import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict

# Descargar recursos de NLTK
nltk.download('punkt')
nltk.download('stopwords')

def word_frequency_summarizer(text, num_sentences=3):
    """
    Resumir texto basado en la frecuencia de palabras.

    Args:
        text (str): Texto de entrada para resumir.
        num_sentences (int): Número de oraciones a incluir en el resumen.

    Returns:
        str: El texto resumido.
    """
    # Paso 1: Tokenizar el texto en oraciones y palabras
    sentences = sent_tokenize(text)
    print("Sentences:", sentences)  # Depuración
    
    # Asegurarse de que num_sentences no exceda el número de oraciones
    if num_sentences > len(sentences):
        num_sentences = len(sentences)

    words = word_tokenize(text.lower())
    
    # Paso 2: Crear una tabla de frecuencias de palabras
    stop_words = set(stopwords.words('english'))
    word_frequencies = defaultdict(int)
    
    for word in words:
        if word.isalnum() and word not in stop_words:  # Ignorar stopwords y puntuación
            word_frequencies[word] += 1

    print("Word Frequencies:", dict(word_frequencies))  # Depuración

    # Paso 3: Calcular puntuaciones para cada oración
    sentence_scores = defaultdict(float)
    
    for i, sentence in enumerate(sentences):
        sentence_words = word_tokenize(sentence.lower())
        for word in sentence_words:
            if word in word_frequencies:
                sentence_scores[i] += word_frequencies[word]

    print("Sentence Scores:", dict(sentence_scores))  # Depuración

    # Paso 4: Seleccionar las mejores oraciones
    sorted_indices = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    sorted_indices = sorted(sorted_indices)  # Mantener el orden original de las oraciones
    print("Selected Indices:", sorted_indices)  # Depuración

    # Paso 5: Construir el resumen
    summary = " ".join([sentences[i] for i in sorted_indices])
    return summary



