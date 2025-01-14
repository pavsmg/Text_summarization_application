from flask import Flask, request, jsonify
from flask_cors import CORS
from summarizer import summarizer

# Inicializar Flask
app = Flask(__name__)
CORS(app, resources={r"/summarize": {"origins": "http://localhost:3000"}})

@app.route('/upload_text', methods=['POST'])
def upload_text():
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No se proporcionó texto'}), 400
    return jsonify({"message": "texto recibido correctamente"})



@app.route('/summarize', methods=['POST'])
def summarize():

    if request.method == 'OPTIONS':
        print("Options preflight request received")
        return jsonify ({"message": "Preflight check successful"}), 200
    
    data = request.json
    print(f"Received data: {data}")

    text = data.get('text')
    technique = data.get('technique')

    if not text or not technique:
        return jsonify({'error': 'No se proporcionó texto o técnica'}), 400
    
    try: 
        summarized_text = summarizer(text, technique, num_sentences=3)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    return jsonify({"summary": summarized_text}) 

# Iniciar el servidor
if __name__ == "__main__":
    app.run(debug=True)
