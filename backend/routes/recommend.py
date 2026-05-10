from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import UserProfile
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

router = APIRouter()

@router.post("/recommend/{email}")
def get_recommendations(email: str, db: Session = Depends(get_db)):
    profile = db.query(UserProfile).filter(UserProfile.email == email).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    prompt = f"""
You are an expert career advisor for senior IT professionals.
Generate exactly 3 personalized career path recommendations.
At least one must be a leadership transition.

Profile:
- Name: {profile.name}
- Current Role: {profile.current_role}
- Years of Experience: {profile.years_of_experience}
- Technical Skills: {profile.technical_skills}
- Soft Skills: {profile.soft_skills}
- Career Motivators: {profile.career_motivators}
- Personality Traits: {profile.personality_traits}
- EQ Self Awareness: {profile.eq_self_awareness}/10
- EQ Empathy: {profile.eq_empathy}/10
- EQ Self Regulation: {profile.eq_self_regulation}/10
- EQ Motivation: {profile.eq_motivation}/10

Respond in this exact format:

RECOMMENDATION 1:
Title: [Role Title]
Type: [Technical Growth / Leadership Transition / Domain Pivot]
Why This Fits: [2-3 sentences]
Key Skills to Develop: [comma separated list]
Timeline: [e.g. 12-18 months]

RECOMMENDATION 2:
Title: [Role Title]
Type: [Technical Growth / Leadership Transition / Domain Pivot]
Why This Fits: [2-3 sentences]
Key Skills to Develop: [comma separated list]
Timeline: [e.g. 6-12 months]

RECOMMENDATION 3:
Title: [Role Title]
Type: [Technical Growth / Leadership Transition / Domain Pivot]
Why This Fits: [2-3 sentences]
Key Skills to Develop: [comma separated list]
Timeline: [e.g. 18-24 months]
"""

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )
    return {"recommendations": response.text}