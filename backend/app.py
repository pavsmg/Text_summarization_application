from flask import Flask, request, jsonify
from flask_cors import CORS


# Inicializar Flask
app = Flask(__name__)
CORS(app)

@app.route('/upload_text', methods=['POST'])
def upload_text():
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No se proporcionó texto'}), 400
    return jsonify({"message": "texto recibido correctamente"})

@app.route('/summerize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text')
    technique = data.get('technique')
    if not text or not technique:
        return jsonify({'error': 'No se proporcionó texto o técnica'}), 400
    
    ## Aquí se selecciona la técnica para resumir el texto
    summarized_text = ""
    '''
    if technique == "TF-IDF":
        summarized_text = extract_keywords_tfidf()
    elif technique == "TextRank":
        summarized_text = extract_keywords_textrank()
    elif technique == "BART":
    '''

    summarized_text = f"Resumen generado con {technique}: {text}"
    return jsonify({"summary": summarized_text}) 

# Iniciar el servidor
if __name__ == "__main__":
    app.run(debug=True)
