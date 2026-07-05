import { useState } from "react"
import { useNavigate } from "react-router-dom"
import API from "../utils/axios"
import toast from "react-hot-toast"

const initialForm = {
  name: "",
  email: "",
  years_of_experience: "",
  current_role: "",
  technical_skills: "",
  soft_skills: "",
  career_motivators: "",
  personality_traits: "",
  eq_self_awareness: 5,
  eq_empathy: 5,
  eq_self_regulation: 5,
  eq_motivation: 5,
}

export default function AssessmentPage() {
  const [formData, setFormData] = useState(initialForm)
  const [loading, setLoading] = useState(false)
  const [submittedEmail, setSubmittedEmail] = useState("")
  const [resumeFile, setResumeFile] = useState(null)
  const [parsing, setParsing] = useState(false)
  const navigate = useNavigate()

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleResumeChange = (e) => {
    setResumeFile(e.target.files[0])
  }

  const handleParseResume = async () => {
    if (!resumeFile) {
      toast.error("Please choose a PDF file first")
      return
    }

    setParsing(true)
    try {
      const fd = new FormData()
      fd.append("file", resumeFile)

      const res = await API.post("/api/resume/parse", fd, {
        headers: { "Content-Type": "multipart/form-data" },
      })

      setFormData((prev) => ({
        ...prev,
        current_role: res.data.current_role || prev.current_role,
        years_of_experience: res.data.years_of_experience ?? prev.years_of_experience,
        technical_skills: res.data.technical_skills || prev.technical_skills,
        soft_skills: res.data.soft_skills || prev.soft_skills,
        career_motivators: res.data.career_motivators || prev.career_motivators,
        personality_traits: res.data.personality_traits || prev.personality_traits,
      }))

      toast.success("Resume parsed! Review the pre-filled fields below.")
    } catch (err) {
      toast.error(err.response?.data?.detail || "Failed to parse resume")
    } finally {
      setParsing(false)
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    try {
      await API.post("/api/profile", {
        ...formData,
        years_of_experience: parseInt(formData.years_of_experience),
        eq_self_awareness: parseInt(formData.eq_self_awareness),
        eq_empathy: parseInt(formData.eq_empathy),
        eq_self_regulation: parseInt(formData.eq_self_regulation),
        eq_motivation: parseInt(formData.eq_motivation),
      })
      toast.success("Profile created successfully!")
      setSubmittedEmail(formData.email)
      setFormData(initialForm)
    } catch (err) {
      toast.error(err.response?.data?.detail || "Something went wrong")
    } finally {
      setLoading(false)
    }
  }

  const eqFields = [
    { label: "Self Awareness", name: "eq_self_awareness" },
    { label: "Empathy", name: "eq_empathy" },
    { label: "Self Regulation", name: "eq_self_regulation" },
    { label: "Motivation", name: "eq_motivation" },
  ]

  return (
    <div style={{ background: "#f5f4f0", minHeight: "100vh", padding: "40px 16px" }}>
      <div style={{ maxWidth: 680, margin: "0 auto", background: "#fff", borderRadius: 16, padding: 40, boxShadow: "0 4px 24px rgba(0,0,0,0.07)" }}>

        <h1 style={{ fontFamily: "DM Serif Display, serif", fontSize: 32, color: "#111", marginBottom: 4 }}>
          Career Path Assessment
        </h1>
        <p style={{ fontFamily: "DM Sans, sans-serif", color: "#666", fontSize: 14, marginBottom: 32 }}>
          5-Dimensional Profile for Senior IT Professionals
        </p>

        <form onSubmit={handleSubmit} style={{ fontFamily: "DM Sans, sans-serif" }}>

          {/* Resume Upload - Optional */}
          <div style={{ marginBottom: 28, padding: 20, background: "#f9f9f7", borderRadius: 12, border: "1px dashed #d1d5db" }}>
            <p style={{ fontSize: 11, fontWeight: 600, letterSpacing: "0.1em", textTransform: "uppercase", color: "#6366F1", marginBottom: 10 }}>
              Optional — Upload Resume to Pre-fill
            </p>
            <div style={{ display: "flex", gap: 10, alignItems: "center", flexWrap: "wrap" }}>
              <input
                type="file"
                accept="application/pdf"
                onChange={handleResumeChange}
                style={{ fontSize: 13, fontFamily: "DM Sans, sans-serif" }}
              />
              <button
                type="button"
                onClick={handleParseResume}
                disabled={parsing}
                style={{ background: "#6366F1", color: "#fff", border: "none", borderRadius: 999, padding: "8px 20px", fontSize: 13, fontFamily: "DM Sans, sans-serif", fontWeight: 600, cursor: parsing ? "not-allowed" : "pointer", opacity: parsing ? 0.6 : 1 }}
              >
                {parsing ? "Parsing..." : "Parse Resume"}
              </button>
            </div>
          </div>

          {/* Basic Info */}
          <div style={{ marginBottom: 28 }}>
            <p style={{ fontSize: 11, fontWeight: 600, letterSpacing: "0.1em", textTransform: "uppercase", color: "#6366F1", marginBottom: 12 }}>
              Basic Information
            </p>
            <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
              {[
                { name: "name", placeholder: "Full Name" },
                { name: "email", type: "email", placeholder: "Email Address" },
                { name: "years_of_experience", type: "number", placeholder: "Years of Experience" },
                { name: "current_role", placeholder: "Current Role (e.g. Senior Software Engineer)" },
              ].map((f) => (
                <input
                  key={f.name}
                  name={f.name}
                  type={f.type || "text"}
                  placeholder={f.placeholder}
                  value={formData[f.name]}
                  onChange={handleChange}
                  required
                  style={{ width: "100%", border: "1px solid #e5e7eb", borderRadius: 8, padding: "10px 14px", fontSize: 14, fontFamily: "DM Sans, sans-serif", outline: "none", boxSizing: "border-box" }}
                />
              ))}
            </div>
          </div>

          {/* Dimensions 1-4 */}
          {[
            { label: "Dimension 1 — Technical Skills", name: "technical_skills", placeholder: "e.g. Python, React, AWS, System Design" },
            { label: "Dimension 2 — Soft Skills", name: "soft_skills", placeholder: "e.g. Communication, Leadership, Mentoring" },
            { label: "Dimension 3 — Career Motivators", name: "career_motivators", placeholder: "e.g. Growth, Innovation, Impact" },
            { label: "Dimension 4 — Personality Traits", name: "personality_traits", placeholder: "e.g. Analytical, Detail-oriented, Collaborative" },
          ].map((d) => (
            <div key={d.name} style={{ marginBottom: 28 }}>
              <p style={{ fontSize: 11, fontWeight: 600, letterSpacing: "0.1em", textTransform: "uppercase", color: "#6366F1", marginBottom: 12 }}>
                {d.label}
              </p>
              <textarea
                name={d.name}
                placeholder={d.placeholder}
                value={formData[d.name]}
                onChange={handleChange}
                required
                style={{ width: "100%", border: "1px solid #e5e7eb", borderRadius: 8, padding: "10px 14px", fontSize: 14, fontFamily: "DM Sans, sans-serif", outline: "none", height: 90, resize: "none", boxSizing: "border-box" }}
              />
            </div>
          ))}

          {/* Dimension 5 - EQ */}
          <div style={{ marginBottom: 28 }}>
            <p style={{ fontSize: 11, fontWeight: 600, letterSpacing: "0.1em", textTransform: "uppercase", color: "#6366F1", marginBottom: 12 }}>
              Dimension 5 — Emotional Intelligence (EQ)
            </p>
            <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
              {eqFields.map((eq) => (
                <div key={eq.name}>
                  <div style={{ display: "flex", justifyContent: "space-between", fontSize: 14, color: "#444", marginBottom: 4 }}>
                    <span>{eq.label}</span>
                    <span style={{ fontWeight: 600, color: "#6366F1" }}>{formData[eq.name]}/10</span>
                  </div>
                  <input
                    type="range"
                    name={eq.name}
                    min="1"
                    max="10"
                    value={formData[eq.name]}
                    onChange={handleChange}
                    style={{ width: "100%", accentColor: "#6366F1" }}
                  />
                </div>
              ))}
            </div>
          </div>

          <button
            type="submit"
            disabled={loading}
            style={{ width: "100%", background: "#111", color: "#fff", border: "none", borderRadius: 999, padding: "14px 0", fontSize: 15, fontFamily: "DM Sans, sans-serif", fontWeight: 600, cursor: loading ? "not-allowed" : "pointer", opacity: loading ? 0.6 : 1 }}
          >
            {loading ? "Submitting..." : "Submit Profile"}
          </button>

        </form>

        {submittedEmail && (
          <div style={{ marginTop: 24, textAlign: "center" }}>
            <p style={{ fontFamily: "DM Sans, sans-serif", color: "#444", fontSize: 14, marginBottom: 12 }}>
              Profile saved! Ready to get your career recommendations?
            </p>
            <button
              onClick={() => navigate(`/recommend/${submittedEmail}`)}
              style={{ background: "#6366F1", color: "#fff", border: "none", borderRadius: 999, padding: "12px 32px", fontSize: 14, fontFamily: "DM Sans, sans-serif", fontWeight: 600, cursor: "pointer" }}
            >
              Get My Recommendations →
            </button>
          </div>
        )}

      </div>
    </div>
  )
}