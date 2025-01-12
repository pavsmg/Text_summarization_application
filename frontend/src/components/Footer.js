import React from 'react';

function Footer() {
    return (
        <footer className="bg-blue-900 text-gray-300 py-6">
            <div className="container mx-auto text-center">
                {/* Social Media Icons */}
                <div className="flex justify-center gap-6 mb-4">
                    <a
                        href="https://github.com"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="hover:text-white transition"
                        aria-label="GitHub"
                    >
                        <i className="fab fa-github text-2xl"></i>
                    </a>
                    <a
                        href="https://twitter.com"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="hover:text-white transition"
                        aria-label="Twitter"
                    >
                        <i className="fab fa-twitter text-2xl"></i>
                    </a>
                    <a
                        href="mailto:support@alphaomega.com"
                        className="hover:text-white transition"
                        aria-label="Email"
                    >
                        <i className="fas fa-envelope text-2xl"></i>
                    </a>
                </div>

                {/* Copyright Text */}
                <p className="text-sm md:text-base">
                    &copy; 2025 Andrade Granados Daniela - Huerta Villanueva Oscar - Juárez Solano Juan Martín - Montoya Gutiérrez Pavel.
                </p>
            </div>
        </footer>
    );
}

export default Footer;
