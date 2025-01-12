import React from "react";

function TechniquesTable({ closeTable }) {
  const techniques = [
    { name: "TF-IDF", type: "Extractivo", complexity: "Baja", library: "scikit-learn" },
    { name: "TextRank", type: "Extractivo", complexity: "Media", library: "Gensim / Sumy" },
    { name: "LSA", type: "Extractivo", complexity: "Media", library: "scikit-learn" },
    { name: "BERT", type: "Abstractivo", complexity: "Alta", library: "Hugging Face" },
    { name: "Frecuencia de palabras", type: "Extractivo", complexity: "Baja", library: "NLTK" },
  ];

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
      <div className="bg-white rounded-lg shadow-lg p-6 w-3/4">
        <h2 className="text-2xl font-bold text-blue-800 mb-4 text-center">
          Conoce más acerca de las técnicas
        </h2>
        <table className="table-auto w-full border-collapse border border-gray-300 text-left">
          <thead>
            <tr className="bg-blue-100">
              <th className="border border-gray-300 px-4 py-2">Técnica</th>
              <th className="border border-gray-300 px-4 py-2">Tipo</th>
              <th className="border border-gray-300 px-4 py-2">Complejidad</th>
              <th className="border border-gray-300 px-4 py-2">Biblioteca usada</th>
            </tr>
          </thead>
          <tbody>
            {techniques.map((technique, index) => (
              <tr key={index} className={index % 2 === 0 ? "bg-gray-50" : "bg-white"}>
                <td className="border border-gray-300 px-4 py-2">{technique.name}</td>
                <td className="border border-gray-300 px-4 py-2">{technique.type}</td>
                <td className="border border-gray-300 px-4 py-2">{technique.complexity}</td>
                <td className="border border-gray-300 px-4 py-2">{technique.library}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <div className="flex justify-center mt-4">
          <button
            onClick={closeTable} // Aquí se llama correctamente la función para cerrar la tabla
            className="px-6 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 focus:ring-2 focus:ring-red-400"
          >
            Cerrar
          </button>
        </div>
      </div>
    </div>
  );
}

export default TechniquesTable;
