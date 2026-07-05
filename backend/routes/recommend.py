from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from google import genai
import os
from dotenv import load_dotenv
from backend.database import get_db
from backend.models import UserProfile
from backend.vector_store import search_benchmarks

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

router = APIRouter()


@router.post("/recommend/{email}")
def get_recommendations(email: str, db: Session = Depends(get_db)):
    profile = db.query(UserProfile).filter(UserProfile.email == email).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    # Step A: build a short query summarizing the profile, for retrieval
    query_text = f"{profile.current_role}, {profile.years_of_experience} years experience, skills: {profile.technical_skills}"

    # Step B: retrieve the most relevant skill-benchmark docs from ChromaDB
    retrieved_docs = search_benchmarks(query_text, top_k=3)
    retrieved_context = "\n\n---\n\n".join(retrieved_docs)

    # Step C: build the prompt, now grounded in retrieved context
    prompt = f"""
You are an expert career advisor for senior IT professionals.

Here are relevant role/level benchmark documents retrieved from a knowledge base:
{retrieved_context}

User Profile:
- Name: {profile.name}
- Current Role: {profile.current_role}
- Years of Experience: {profile.years_of_experience}
- Technical Skills: {profile.technical_skills}
- Soft Skills: {profile.soft_skills}
- Career Motivators: {profile.career_motivators}
- Personality Traits: {profile.personality_traits}
- EQ Scores (out of 10): Self-Awareness {profile.eq_self_awareness}, Empathy {profile.eq_empathy}, Self-Regulation {profile.eq_self_regulation}, Motivation {profile.eq_motivation}

Using the retrieved benchmark documents above as ground truth for what's expected at each level,
identify the specific gap between the user's current skills and the next level's expectations,
then generate 3 career path recommendations.

Respond in this exact format:
RECOMMENDATION 1:
Title: ...
Type: ...
Why This Fits: ...
Skill Gap Identified: ...
"""

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )
    return {"recommendations": response.text}