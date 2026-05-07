from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from backend.database import Base

class UserProfile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    years_of_experience = Column(Integer, nullable=False)
    current_role = Column(String, nullable=False)
    technical_skills = Column(Text, nullable=False)
    soft_skills = Column(Text, nullable=False)
    career_motivators = Column(Text, nullable=False)
    personality_traits = Column(Text, nullable=False)
    eq_self_awareness = Column(Integer, nullable=False)
    eq_empathy = Column(Integer, nullable=False)
    eq_self_regulation = Column(Integer, nullable=False)
    eq_motivation = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)