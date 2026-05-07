from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from backend.database import get_db
from backend.models import UserProfile

router = APIRouter()

class ProfileCreate(BaseModel):
    name: str
    email: str
    years_of_experience: int
    current_role: str
    technical_skills: str
    soft_skills: str
    career_motivators: str
    personality_traits: str
    eq_self_awareness: int
    eq_empathy: int
    eq_self_regulation: int
    eq_motivation: int

@router.post("/profile")
def create_profile(profile: ProfileCreate, db: Session = Depends(get_db)):
    existing = db.query(UserProfile).filter(UserProfile.email == profile.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Profile with this email already exists")
    
    new_profile = UserProfile(**profile.model_dump())
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return {"message": "Profile created successfully", "id": new_profile.id}

@router.get("/profile/{email}")
def get_profile(email: str, db: Session = Depends(get_db)):
    profile = db.query(UserProfile).filter(UserProfile.email == email).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile