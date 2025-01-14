import React, { useState } from "react";
import Header from "../components/Header";
import Sidebar from "../components/Sidebar";
import Footer from "../components/Footer";
import TechniquesTable from "../components/TechniquesTable";

function TextSummarizer() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [uploadedText, setUploadedText] = useState("");
  const [summary, setSummary] = useState("");
  const [processing, setProcessing] = useState(false);
  const [selectedTechnique, setSelectedTechnique] = useState("");
  const [showTable, setShowTable] = useState(false);

  const toggleSidebar = () => {
    setIsSidebarOpen((prev) => !prev);
  };

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      if (!file.name.endsWith(".txt")) {
        alert("Please upload a valid .txt file.");
        return;
      }
      const reader = new FileReader();
      reader.onload = (e) => {
        setUploadedText(e.target.result);
      };
      reader.readAsText(file);
    }
  };

  const handleTechniqueChange = (event) => {
    setSelectedTechnique(event.target.value);
  };

  const handleSummarize = async () => {
    if (!uploadedText || !selectedTechnique) {
      alert("Please upload text and select a technique.");
      return;
    }

    setProcessing(true);

    try {
      const response = await fetch("http://127.0.0.1:5000/summarize", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: uploadedText,
          technique: selectedTechnique,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        setSummary(data.summary);
      } else {
        alert(`Error: ${data.error || "Something went wrong"}`);
      }
    } catch (error) {
      alert(`Error: ${error.message || "Unable to connect to the server"}`);
    } finally {
      setProcessing(false);
    }
  };

  return (
    <div className="bg-gradient-to-br from-gray-50 to-gray-200 min-h-screen flex flex-col relative font-sans">
      <Header />
      <Sidebar isOpen={isSidebarOpen} toggleSidebar={toggleSidebar} />
      <main className="flex-1 flex flex-row gap-8 p-6">
        <div className="flex flex-col gap-4 w-1/4">
          <div className="bg-white p-4 rounded-lg shadow-xl border border-gray-300">
            <h3 className="text-blue-600 font-bold text-center mb-4 text-lg">
              Cargar archivo
            </h3>
            <input
              type="file"
              accept=".txt"
              onChange={handleFileUpload}
              className="block w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-400"
            />
          </div>

          <div className="bg-white p-4 rounded-lg shadow-xl border border-gray-300">
            <h3 className="text-blue-600 font-bold text-center mb-4 text-lg">
              Seleccionar técnica
            </h3>
            <select
              value={selectedTechnique}
              onChange={handleTechniqueChange}
              className="block w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-400"
            >
              <option value="">-- Selecciona una técnica --</option>
              <option value="TF-IDF">TF-IDF</option>
              <option value="WordFreq">Frecuencia de palabras</option>
              <option value="TextRank">TextRank</option>
              <option value="LSA">Latent Semantic Analysis (LSA)</option>
              <option value="BERT">BERT para resumen</option>
            </select>
          </div>

          <button
            onClick={handleSummarize}
            className="py-2 px-4 rounded-md bg-blue-500 text-white font-semibold hover:bg-blue-600 transition shadow-md focus:ring-2 focus:ring-blue-400"
            disabled={processing || !uploadedText || !selectedTechnique}
          >
            {processing ? "Procesando..." : "Generar Resumen"}
          </button>
        </div>

        <div className="flex flex-row gap-4 w-3/4">
          <div className="bg-white p-6 rounded-lg shadow-xl border border-gray-300 w-1/2">
            <h3 className="text-blue-600 font-bold text-center mb-4 text-lg">
              Texto original
            </h3>
            <pre className="whitespace-pre-wrap text-sm text-gray-800 overflow-y-auto max-h-96">
              {uploadedText || "El texto cargado aparecerá aquí."}
            </pre>
          </div>

          <div className="bg-white p-6 rounded-lg shadow-xl border border-gray-300 w-1/2">
            <h3 className="text-blue-600 font-bold text-center mb-4 text-lg">
              Texto resumido
            </h3>
            <pre className="whitespace-pre-wrap text-sm text-gray-800 overflow-y-auto max-h-96">
              {summary || "El resumen aparecerá aquí."}
            </pre>
          </div>
        </div>
      </main>

      {showTable && <TechniquesTable closeTable={() => setShowTable(false)} />}
      <Footer />
    </div>
  );
}

export default TextSummarizer;
