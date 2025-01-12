# Text summarization application

This project is a text summarization application built with Flask and React. It provides an API to upload text and summarize it using different techniques.

- TF-IDF
- TextRank
- LSA
- BERT
- Word Frequency

## Project Structure

Text_summarization_application/ 
│ ├── backend/ 
│ ├── app.py 
│ ├── preprocessing.py 
│ ├── techniques/ 
│ │ ├── init.py 
│ │ ├── technique1.py 
│ │ └── technique2.py 
│ └── requirements.txt 
├── frontend/ 
│ ├── public/ 
│ ├── src/ 
│ ├── package.json 
│ └── ... 
└── README.md

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/text_summarization_application.git
    cd text_summarization_application
    ```

2. Set up the backend:
    ```sh
    cd backend
    python -m venv venv
    venv\Scripts\activate  # On Windows
    pip install -r requirements.txt
    ```

3. Set up the frontend:
    ```sh
    cd ../frontend
    npm install
    ````

## Usage

1. Run the frontend:
    ```sh
    cd frontend
    npm start
    ```

2. Run the backend:
    ```sh
    cd ../backend
    python app.py
    ```

3. The frontend will be available at `http://localhost:3000` and the API will be available at `http://127.0.0.1:5000`.


### Endpoints

- **POST /upload_text**
    - Request Body: `{ "text": "your text here" }`
    - Response: `{ "message": "texto recibido correctamente" }`

- **POST /summarize**
    - Request Body: `{ "text": "your text here", "technique": "technique1" }`
    - Response: `{ "summary": "your summarized text here" }`

## Techniques

The summarization techniques are implemented in the `techniques` folder. You can add more techniques by creating new files.

## Preprocessing

The [preprocessing.py] file contains functions for text preprocessing, including tokenization, stopword removal, stemming, and lemmatization.

## License

This project is licensed under the MIT License. See the LICENSE file for details.