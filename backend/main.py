# it turns on the server, builds the database table if it's missing, and decides who's allowed to knock.
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from backend.database import engine, Base
from backend.routes import profile, recommend
from backend.routes import profile, recommend, resume

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Intelligent Career Path Advisory Agent") # this actually creates the running application object

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(profile.router, prefix="/api")
app.include_router(recommend.router, prefix="/api")
app.include_router(resume.router, prefix="/api")