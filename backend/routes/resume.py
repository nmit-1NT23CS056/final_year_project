from fastapi import APIRouter, UploadFile, File, HTTPException
from google import genai
import pdfplumber
import os
import io
import json
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

router = APIRouter()


def extract_text_from_pdf(file_bytes: bytes) -> str:
    text = ""
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()


@router.post("/resume/parse")
async def parse_resume(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    file_bytes = await file.read()

    try:
        resume_text = extract_text_from_pdf(file_bytes)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not read PDF: {str(e)}")

    if not resume_text:
        raise HTTPException(status_code=400, detail="No extractable text found in this PDF")

    prompt = f"""
You are an information extraction system. Given the raw resume text below,
extract the following fields and respond with ONLY valid JSON — no markdown, no explanation.

Fields:
- current_role: string, most recent/current job title
- years_of_experience: integer, best estimate of total years of professional experience
- technical_skills: string, comma-separated technical skills found
- soft_skills: string, comma-separated soft skills found or reasonably inferred
- career_motivators: string, comma-separated likely motivators inferred (e.g. growth, leadership, innovation)
- personality_traits: string, comma-separated personality traits reasonably inferred from tone/content

Resume text:
\"\"\"
{resume_text[:6000]}
\"\"\"

Respond with ONLY this exact JSON shape:
{{
  "current_role": "...",
  "years_of_experience": 0,
  "technical_skills": "...",
  "soft_skills": "...",
  "career_motivators": "...",
  "personality_traits": "..."
}}
"""

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )

    raw = response.text.strip()

    # Gemini sometimes wraps JSON in ```json fences even when told not to — strip defensively
    if raw.startswith("```"):
        raw = raw.strip("`")
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        raise HTTPException(status_code=502, detail="Failed to parse AI response as JSON")

    return parsed