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
      const reader = new FileReader();
      reader.onload = (e) => {
        setUploadedText(e.target.result);
      };
      reader.readAsText(file);
    }
  };

  const handleSummarize = () => {
    if (!uploadedText) {
      alert("Primero sube un archivo de texto.");
      return;
    }

    if (!selectedTechnique) {
      alert("Selecciona una técnica para el resumen.");
      return;
    }

    setProcessing(true);
    setTimeout(() => {
      setSummary(`Resumen generado usando la técnica: ${selectedTechnique}`);
      setProcessing(false);
    }, 2000);
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
              onChange={(e) => setSelectedTechnique(e.target.value)}
              className="block w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-400"
            >
              <option value="">-- Selecciona una técnica --</option>
              <option value="TF-IDF">TF-IDF</option>
              <option value="Frecuencia de palabras">Frecuencia de palabras</option>
              {/* <option value="Rake">Rake</option> */}
              <option value="TextRank">TextRank</option>
              <option value="Latent Semantic Analysis (LSA)">Latent Semantic Analysis (LSA)</option>
              <option value="BERT para resumen">BERT para resumen</option>
            </select>
          </div>

          <button
            onClick={handleSummarize}
            className="py-2 px-4 rounded-md bg-blue-500 text-white font-semibold hover:bg-blue-600 transition shadow-md focus:ring-2 focus:ring-blue-400"
            disabled={processing}
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

        {/* Botón para mostrar/ocultar la tabla */}
        <div className="text-center mt-4 mb-6">
          <button
            onClick={() => setShowTable(true)}
            className="py-2 px-4 bg-blue-500 text-white rounded-md font-semibold hover:bg-blue-600"
          >
            Conocer más acerca de las técnicas
          </button>
        </div>


        {/* Tabla de técnicas (solo si showTable es true) */}
        {showTable && <TechniquesTable closeTable={() => setShowTable(false)} />}

      <Footer />
    </div>
  );
}

export default TextSummarizer;
