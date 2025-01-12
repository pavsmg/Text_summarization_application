import React from "react";

function Header({ toggleSidebar }) {
  return (
    <header className="flex items-center justify-between px-6 py-4 bg-blue-800 shadow-lg">
      {/* Botón de hamburguesa (izquierda) */}
      <button
        className="text-3xl text-white lg:hidden focus:outline-none hover:text-gray-300 transition"
        onClick={toggleSidebar}
      >
        ☰
      </button>

      {/* Logo y nombre del equipo (centro) */}
      <div className="flex items-center gap-4 mx-auto">
        <img
          src="/images/text_logo.png"
          alt="AlphaOmega Logo"
          className="w-12 h-12"
        />
        <h1 className="text-2xl font-extrabold text-white tracking-wide">
          Text Summarizer System
        </h1>
      </div>

      {/* Espacio vacío para mantener el diseño */}
      <div className="hidden lg:block w-10"></div>
    </header>
  );
}

export default Header;
