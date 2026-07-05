import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

from backend.graph.state import RecommendationState
from backend.vector_store import search_benchmarks


def profile_analyzer(state: RecommendationState) -> RecommendationState:
    """Builds a clean summary string from raw profile fields, used later for retrieval."""
    summary = (
        f"{state['current_role']}, {state['years_of_experience']} years experience, "
        f"skills: {state['technical_skills']}"
    )
    state["profile_summary"] = summary
    return state


def retriever(state: RecommendationState) -> RecommendationState:
    """Searches ChromaDB for the most relevant skill-benchmark docs, using the profile summary as the query."""
    retrieved = search_benchmarks(state["profile_summary"], top_k=3)
    state["retrieved_docs"] = retrieved
    return state

def recommendation_generator(state: RecommendationState) -> RecommendationState:
    """Calls Gemini using the profile + retrieved benchmark docs as grounding context."""
    retrieved_context = "\n\n---\n\n".join(state["retrieved_docs"])

    prompt = f"""
You are an expert career advisor for senior IT professionals.

Here are relevant role/level benchmark documents retrieved from a knowledge base:
{retrieved_context}

User Profile:
- Current Role: {state['current_role']}
- Years of Experience: {state['years_of_experience']}
- Technical Skills: {state['technical_skills']}
- Soft Skills: {state['soft_skills']}
- Career Motivators: {state['career_motivators']}
- Personality Traits: {state['personality_traits']}
- EQ Scores: {state['eq_scores']}

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
    state["final_recommendations"] = response.text
    return state

def validator(state: RecommendationState) -> RecommendationState:
    """Basic sanity check on Gemini's output before returning it to the user."""
    text = state["final_recommendations"]

    required_markers = ["RECOMMENDATION 1:", "RECOMMENDATION 2:", "RECOMMENDATION 3:"]
    missing = [m for m in required_markers if m not in text]

    if missing:
        state["final_recommendations"] += (
            f"\n\n[Note: response may be incomplete — missing sections: {', '.join(missing)}]"
        )

    return state