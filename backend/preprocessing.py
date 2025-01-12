import string
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Descargar recursos necesarios
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Stemmer 
stemmer = PorterStemmer()

# Función para convertir etiquetas POS de nltk a las de wordnet
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Si no hay etiqueta, usar sustantivo como default

lemmatizer = WordNetLemmatizer()

def apply_lemmatization(tagged_text):
    lemmatized_words = []
    for word, tag in tagged_text:
        wordnet_pos = get_wordnet_pos(tag)  # Convertir etiqueta POS al formato de WordNet
        lemmatized_word = lemmatizer.lemmatize(word, wordnet_pos)  # Aplicar lematización
        lemmatized_words.append(lemmatized_word)
    return lemmatized_words 


def normalization(raw_corpus, pipeline_version):
    """
    Normaliza un corpus de texto aplicando diferentes pipelines de procesamiento.

    Parámetros:
    - raw_corpus: Lista de cadenas de texto (documentos).
    - pipeline_version: Entero que indica la versión del pipeline (1, 2, 3 o 4).

    Retorna:
    - processed_corpus: Lista de listas de tokens procesados.
    """
    processed_corpus = []
    stemmer = PorterStemmer()  # Definir el stemmer si se utiliza en el pipeline

    for document in raw_corpus:
        # Convertir a minúsculas
        document = document.lower()
        # Eliminar números
        document = re.sub(r'\d+', '', document)
        
        if pipeline_version == 1:
            # Pipeline 1: Remover puntuación y stopwords, aplicar stemming
            # Eliminar puntuación
            document = re.sub(r'[^\w\s]', '', document)
            # Tokenización
            tokens = word_tokenize(document)
            # Remover stopwords
            tokens = [word for word in tokens if word not in stop_words]
            # Aplicación de POS-tagging
            tagged_tokens = pos_tag(tokens)
            # Aplicación de stemming
            stemmed_tokens = [stemmer.stem(word) for word, tag in tagged_tokens]
            processed_corpus.append(stemmed_tokens)

        elif pipeline_version == 2:
            # Pipeline 2: Remover puntuación y stopwords, aplicar lematización
            # Eliminar puntuación
            document = re.sub(r'[^\w\s]', '', document)
            # Tokenización
            tokens = word_tokenize(document)
            # Remover stopwords
            tokens = [word for word in tokens if word not in stop_words]
            # Aplicación de POS-tagging
            tagged_tokens = pos_tag(tokens)
            # Aplicación de lematización
            lemmatized_tokens = apply_lemmatization(tagged_tokens)
            processed_corpus.append(lemmatized_tokens)

        elif pipeline_version == 3:
            # Pipeline 3: Remover stopwords, aplicar lematización
            # Tokenización
            tokens = word_tokenize(document)
            # Remover stopwords
            tokens = [word for word in tokens if word not in stop_words]
            # Aplicación de POS-tagging
            tagged_tokens = pos_tag(tokens)
            # Aplicación de lematización
            lemmatized_tokens = apply_lemmatization(tagged_tokens)
            processed_corpus.append(lemmatized_tokens)

        elif pipeline_version == 4:
            # Pipeline 4: Remover puntuación y stopwords sin stemming ni lematización
            # Tokenización
            tokens = word_tokenize(document)
            # Eliminar puntuación
            tokens = [word for word in tokens if word not in string.punctuation]
            # Remover stopwords
            tokens = [word for word in tokens if word not in stop_words]
            processed_corpus.append(tokens)

        else:
            print("Por favor, elige una versión de pipeline válida (1, 2, 3 o 4).")
            return None

    return processed_corpus

print(processed_corpus)

processed_corpus = normalization(text_corpus, 4)