import { BrowserRouter, Routes, Route } from "react-router-dom"
import { Toaster } from "react-hot-toast"
import AssessmentPage from "./pages/AssessmentPage"
import RecommendPage from "./pages/RecommendPage"

export default function App() {
  return (
    <BrowserRouter>
      <Toaster position="top-right" />
      <Routes>
        <Route path="/" element={<AssessmentPage />} />
        <Route path="/recommend/:email" element={<RecommendPage />} />
      </Routes>
    </BrowserRouter>
  )
}