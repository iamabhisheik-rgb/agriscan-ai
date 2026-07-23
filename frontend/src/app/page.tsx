"use client";

import { useState } from "react";

export default function Home() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  // Handle file selection
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      setSelectedFile(file);
      setPreview(URL.createObjectURL(file)); // Create a local URL to preview the image
      setResult(null);
      setError(null);
    }
  };

  // Send image to backend
  const handleAnalyze = async () => {
    if (!selectedFile) {
      setError("Please select an image first.");
      return;
    }

    setLoading(true);
    setError(null);

    // We must use FormData to send files in HTTP requests
    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await fetch("http://localhost:8000/api/scans/analyze", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Failed to analyze image. Backend error.");
      }

      const data = await response.json();
      setResult(data);
    } catch (err: any) {
      setError(err.message || "An unknown error occurred.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-green-50 via-emerald-50 to-teal-50 py-12 px-4">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-green-600 to-emerald-500 mb-3">
            AgriScan AI 🌿
          </h1>
          <p className="text-lg text-gray-600">
            Upload a photo of your crop to instantly detect pests and diseases.
          </p>
        </div>

        {/* Upload Card */}
        <div className="bg-white rounded-2xl shadow-xl border border-gray-100 p-8 mb-8 backdrop-blur-sm">
          <div className="flex flex-col items-center justify-center space-y-6">
            
            {/* Image Preview Area */}
            {preview ? (
              <img 
                src={preview} 
                alt="Selected plant" 
                className="max-h-80 rounded-xl object-contain border-2 border-green-200 shadow-sm"
              />
            ) : (
              <div className="w-full h-64 border-2 border-dashed border-green-300 rounded-xl flex items-center justify-center bg-green-50/50">
                <p className="text-gray-400">No image selected yet</p>
              </div>
            )}

            {/* Buttons */}
            <div className="flex flex-col sm:flex-row gap-4 w-full justify-center">
              <label className="cursor-pointer bg-white border-2 border-green-500 text-green-600 font-semibold py-3 px-6 rounded-lg hover:bg-green-50 transition duration-300 text-center">
                {selectedFile ? "Change Image" : "Upload Image"}
                <input type="file" accept="image/*" onChange={handleFileChange} className="hidden" />
              </label>
              
              <button 
                onClick={handleAnalyze}
                disabled={!selectedFile || loading}
                className={`font-semibold py-3 px-8 rounded-lg text-white transition duration-300 ${
                  !selectedFile || loading ? "bg-gray-400 cursor-not-allowed" : "bg-gradient-to-r from-green-600 to-emerald-500 hover:from-green-700 hover:to-emerald-600 shadow-lg"
                }`}
              >
                {loading ? "🧠 AI Analyzing..." : "Analyze Plant"}
              </button>
            </div>

            {error && <p className="text-red-500 font-medium">{error}</p>}
          </div>
        </div>

        {/* Results Card */}
        {result && !loading && (
          <div className="bg-white rounded-2xl shadow-xl border border-gray-100 p-8 animate-fade-in-up">
            <h2 className="text-2xl font-bold text-gray-800 mb-6 flex items-center gap-2">
              🩺 Diagnosis Report
            </h2>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="bg-green-50 p-4 rounded-lg">
                <h3 className="text-sm font-medium text-gray-500">Disease / Pest</h3>
                <p className="text-xl font-bold text-green-700 mt-1">{result.disease_name || "Unknown"}</p>
              </div>
              
              <div className="bg-blue-50 p-4 rounded-lg">
                <h3 className="text-sm font-medium text-gray-500">Confidence Score</h3>
                <p className="text-xl font-bold text-blue-700 mt-1">{result.confidence_score || "N/A"}</p>
              </div>
            </div>

            <div className="mt-6">
              <h3 className="text-lg font-semibold text-gray-800 mb-2">Description</h3>
              <p className="text-gray-600 bg-gray-50 p-4 rounded-lg">{result.description || "No description available."}</p>
            </div>

            <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="bg-emerald-50 p-4 rounded-lg border border-emerald-100">
                <h3 className="text-lg font-semibold text-emerald-800 mb-2">🌿 Organic Treatment</h3>
                <p className="text-gray-700 text-sm">{result.organic_treatment || "N/A"}</p>
              </div>
              
              <div className="bg-orange-50 p-4 rounded-lg border border-orange-100">
                <h3 className="text-lg font-semibold text-orange-800 mb-2">🧪 Chemical Treatment</h3>
                <p className="text-gray-700 text-sm">{result.chemical_treatment || "N/A"}</p>
              </div>
            </div>
          </div>
        )}
      </div>
    </main>
  );
}