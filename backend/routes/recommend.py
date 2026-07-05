from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import UserProfile
from backend.graph.graph import recommendation_graph

router = APIRouter()


@router.post("/recommend/{email}")
def get_recommendations(email: str, db: Session = Depends(get_db)):
    profile = db.query(UserProfile).filter(UserProfile.email == email).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    eq_scores = (
        f"Self-Awareness {profile.eq_self_awareness}, Empathy {profile.eq_empathy}, "
        f"Self-Regulation {profile.eq_self_regulation}, Motivation {profile.eq_motivation}"
    )

    initial_state = {
        "current_role": profile.current_role,
        "years_of_experience": profile.years_of_experience,
        "technical_skills": profile.technical_skills,
        "soft_skills": profile.soft_skills,
        "career_motivators": profile.career_motivators,
        "personality_traits": profile.personality_traits,
        "eq_scores": eq_scores,
        "profile_summary": "",
        "retrieved_docs": [],
        "final_recommendations": "",
    }

    result_state = recommendation_graph.invoke(initial_state)

    return {"recommendations": result_state["final_recommendations"]}