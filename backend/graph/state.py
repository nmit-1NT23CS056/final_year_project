from typing import TypedDict, List


class RecommendationState(TypedDict):
    profile_summary: str
    technical_skills: str
    years_of_experience: int
    current_role: str
    soft_skills: str
    career_motivators: str
    personality_traits: str
    eq_scores: str
    retrieved_docs: List[str]
    final_recommendations: str