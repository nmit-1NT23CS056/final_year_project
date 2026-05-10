import { useState } from "react"
import axios from "axios"

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

export default function AssessmentForm() {
  const [formData, setFormData] = useState(initialForm)
  const [message, setMessage] = useState("")
  const [error, setError] = useState("")
  const [loading, setLoading] = useState(false)

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setMessage("")
    setError("")

    try {
      const res = await axios.post("http://localhost:8000/api/profile", {
        ...formData,
        years_of_experience: parseInt(formData.years_of_experience),
        eq_self_awareness: parseInt(formData.eq_self_awareness),
        eq_empathy: parseInt(formData.eq_empathy),
        eq_self_regulation: parseInt(formData.eq_self_regulation),
        eq_motivation: parseInt(formData.eq_motivation),
      })
      setMessage(res.data.message)
      setFormData(initialForm)
    } catch (err) {
      setError(err.response?.data?.detail || "Something went wrong")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gray-50 py-10 px-4">
      <div className="max-w-2xl mx-auto bg-white rounded-2xl shadow-md p-8">

        <h1 className="text-3xl font-bold text-gray-900 mb-1">
          Career Path Assessment
        </h1>
        <p className="text-gray-500 mb-8 text-sm">
          5-Dimensional Profile for Senior IT Professionals
        </p>

        <form onSubmit={handleSubmit} className="space-y-8">

          {/* Basic Info */}
          <div>
            <h2 className="text-xs font-semibold uppercase tracking-widest text-indigo-600 mb-4">
              Basic Information
            </h2>
            <div className="space-y-3">
              <input
                name="name"
                placeholder="Full Name"
                value={formData.name}
                onChange={handleChange}
                required
                className="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-indigo-500"
              />
              <input
                name="email"
                type="email"
                placeholder="Email Address"
                value={formData.email}
                onChange={handleChange}
                required
                className="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-indigo-500"
              />
              <input
                name="years_of_experience"
                type="number"
                placeholder="Years of Experience"
                value={formData.years_of_experience}
                onChange={handleChange}
                required
                className="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-indigo-500"
              />
              <input
                name="current_role"
                placeholder="Current Role (e.g. Senior Software Engineer)"
                value={formData.current_role}
                onChange={handleChange}
                required
                className="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-indigo-500"
              />
            </div>
          </div>

          {/* Dimension 1 */}
          <div>
            <h2 className="text-xs font-semibold uppercase tracking-widest text-indigo-600 mb-4">
              Dimension 1 — Technical Skills
            </h2>
            <textarea
              name="technical_skills"
              placeholder="e.g. Python, React, AWS, System Design, Kubernetes"
              value={formData.technical_skills}
              onChange={handleChange}
              required
              className="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-indigo-500 h-24 resize-none"
            />
          </div>

          {/* Dimension 2 */}
          <div>
            <h2 className="text-xs font-semibold uppercase tracking-widest text-indigo-600 mb-4">
              Dimension 2 — Soft Skills
            </h2>
            <textarea
              name="soft_skills"
              placeholder="e.g. Communication, Leadership, Conflict Resolution, Mentoring"
              value={formData.soft_skills}
              onChange={handleChange}
              required
              className="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-indigo-500 h-24 resize-none"
            />
          </div>

          {/* Dimension 3 */}
          <div>
            <h2 className="text-xs font-semibold uppercase tracking-widest text-indigo-600 mb-4">
              Dimension 3 — Career Motivators
            </h2>
            <textarea
              name="career_motivators"
              placeholder="e.g. Growth, Innovation, Work-life balance, Impact"
              value={formData.career_motivators}
              onChange={handleChange}
              required
              className="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-indigo-500 h-24 resize-none"
            />
          </div>

          {/* Dimension 4 */}
          <div>
            <h2 className="text-xs font-semibold uppercase tracking-widest text-indigo-600 mb-4">
              Dimension 4 — Personality Traits
            </h2>
            <textarea
              name="personality_traits"
              placeholder="e.g. Analytical, Detail-oriented, Collaborative, Risk-taker"
              value={formData.personality_traits}
              onChange={handleChange}
              required
              className="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-indigo-500 h-24 resize-none"
            />
          </div>

          {/* Dimension 5 - EQ */}
          <div>
            <h2 className="text-xs font-semibold uppercase tracking-widest text-indigo-600 mb-4">
              Dimension 5 — Emotional Intelligence (EQ)
            </h2>
            <div className="space-y-4">

              {[
                { label: "Self Awareness", name: "eq_self_awareness" },
                { label: "Empathy", name: "eq_empathy" },
                { label: "Self Regulation", name: "eq_self_regulation" },
                { label: "Motivation", name: "eq_motivation" },
              ].map((eq) => (
                <div key={eq.name}>
                  <div className="flex justify-between text-sm text-gray-600 mb-1">
                    <span>{eq.label}</span>
                    <span className="font-semibold text-indigo-600">
                      {formData[eq.name]}/10
                    </span>
                  </div>
                  <input
                    type="range"
                    name={eq.name}
                    min="1"
                    max="10"
                    value={formData[eq.name]}
                    onChange={handleChange}
                    className="w-full accent-indigo-600"
                  />
                </div>
              ))}

            </div>
          </div>

          {/* Messages */}
          {message && (
            <div className="bg-green-50 text-green-700 text-sm px-4 py-3 rounded-lg text-center">
              {message}
            </div>
          )}
          {error && (
            <div className="bg-red-50 text-red-600 text-sm px-4 py-3 rounded-lg text-center">
              {error}
            </div>
          )}

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-indigo-600 hover:bg-indigo-700 disabled:bg-indigo-300 text-white font-semibold py-3 rounded-lg transition-colors cursor-pointer"
          >
            {loading ? "Submitting..." : "Submit Profile"}
          </button>

        </form>
      </div>
    </div>
  )
}