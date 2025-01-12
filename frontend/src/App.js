import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import TextSummarizer from "./pages/TextSummarizer";


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<TextSummarizer />} />
      </Routes>
    </Router>
  );
}

export default App;
