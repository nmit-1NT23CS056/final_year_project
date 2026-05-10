import { useEffect, useState } from "react"
import { useParams, useNavigate } from "react-router-dom"
import API from "../utils/axios"
import toast from "react-hot-toast"

function parseRecommendations(text) {
  const blocks = text.split(/RECOMMENDATION \d+:/).filter(Boolean)
  return blocks.map((block) => {
    const get = (key) => {
      const match = block.match(new RegExp(`${key}:\\s*(.+)`))
      return match ? match[1].trim() : ""
    }
    return {
      title: get("Title"),
      type: get("Type"),
      why: get("Why This Fits"),
      skills: get("Key Skills to Develop"),
      timeline: get("Timeline"),
    }
  })
}

const typeColors = {
  "Leadership Transition": { bg: "#fef3c7", color: "#92400e" },
  "Technical Growth": { bg: "#dbeafe", color: "#1e40af" },
  "Domain Pivot": { bg: "#d1fae5", color: "#065f46" },
}

export default function RecommendPage() {
  const { email } = useParams()
  const navigate = useNavigate()
  const [recommendations, setRecommendations] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetch = async () => {
      try {
        const res = await API.post(`/api/recommend/${email}`)
        const parsed = parseRecommendations(res.data.recommendations)
        setRecommendations(parsed)
      } catch (err) {
        toast.error(err.response?.data?.detail || "Failed to get recommendations")
      } finally {
        setLoading(false)
      }
    }
    fetch()
  }, [email])

  return (
    <div style={{ background: "#f5f4f0", minHeight: "100vh", padding: "40px 16px" }}>
      <div style={{ maxWidth: 720, margin: "0 auto" }}>

        <button
          onClick={() => navigate("/")}
          style={{ fontFamily: "DM Sans, sans-serif", fontSize: 14, color: "#6366F1", background: "none", border: "none", cursor: "pointer", marginBottom: 24, padding: 0 }}
        >
          ← Back to Assessment
        </button>

        <h1 style={{ fontFamily: "DM Serif Display, serif", fontSize: 32, color: "#111", marginBottom: 4 }}>
          Your Career Recommendations
        </h1>
        <p style={{ fontFamily: "DM Sans, sans-serif", color: "#666", fontSize: 14, marginBottom: 32 }}>
          AI-powered paths based on your 5-dimensional profile
        </p>

        {loading ? (
          <div style={{ textAlign: "center", padding: "60px 0", fontFamily: "DM Sans, sans-serif", color: "#666" }}>
            Generating your personalized recommendations...
          </div>
        ) : (
          <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
            {recommendations.map((rec, i) => {
              const typeKey = Object.keys(typeColors).find(k => rec.type?.includes(k)) || "Technical Growth"
              const colors = typeColors[typeKey]
              return (
                <div
                  key={i}
                  style={{ background: "#fff", borderRadius: 16, padding: 28, boxShadow: "0 2px 16px rgba(0,0,0,0.06)" }}
                >
                  <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 12, flexWrap: "wrap", gap: 8 }}>
                    <h2 style={{ fontFamily: "DM Serif Display, serif", fontSize: 22, color: "#111", margin: 0 }}>
                      {i + 1}. {rec.title}
                    </h2>
                    <span style={{ background: colors.bg, color: colors.color, fontSize: 12, fontWeight: 600, padding: "4px 12px", borderRadius: 999, fontFamily: "DM Sans, sans-serif" }}>
                      {rec.type}
                    </span>
                  </div>

                  <p style={{ fontFamily: "DM Sans, sans-serif", fontSize: 14, color: "#444", lineHeight: 1.6, marginBottom: 16 }}>
                    {rec.why}
                  </p>

                  <div style={{ display: "flex", gap: 24, flexWrap: "wrap" }}>
                    <div>
                      <p style={{ fontSize: 11, fontWeight: 600, letterSpacing: "0.08em", textTransform: "uppercase", color: "#6366F1", marginBottom: 4, fontFamily: "DM Sans, sans-serif" }}>
                        Key Skills
                      </p>
                      <p style={{ fontFamily: "DM Sans, sans-serif", fontSize: 13, color: "#555" }}>
                        {rec.skills}
                      </p>
                    </div>
                    <div>
                      <p style={{ fontSize: 11, fontWeight: 600, letterSpacing: "0.08em", textTransform: "uppercase", color: "#6366F1", marginBottom: 4, fontFamily: "DM Sans, sans-serif" }}>
                        Timeline
                      </p>
                      <p style={{ fontFamily: "DM Sans, sans-serif", fontSize: 13, color: "#555" }}>
                        {rec.timeline}
                      </p>
                    </div>
                  </div>
                </div>
              )
            })}
          </div>
        )}

      </div>
    </div>
  )
}