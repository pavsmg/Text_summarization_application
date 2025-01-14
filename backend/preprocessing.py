'''
### Normalization pipeline

Una vez con los textos que queremos resumir, podemos hacer la etapa de normalización. 
Se relizarán dos variaciones de la normalización.

Dependiendo de la técnica de resumen que se elija, 
se utilizará un pipeline de normalización diferente.
Tenemos cuatro, se explican a continuación sus diferencias:

Estructura del pipeline:

Pipeline 1: Remueve puntuación y stopwords, aplica stemming.
Pipeline 2: Remueve puntuación y stopwords, aplica lematización.
Pipeline 3: Remueve stopwords, aplica lematización.
Pipeline 4: No remueve puntuación ni stopwords, aplica lematización
 (especial para el resumen).
'''
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
'''
Preparamos el stemmer y lematizador.
'''
stop_words = set(stopwords.words('english')) # Lista de stopwords en inglés
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# Función para convertir etiquetas POS de nltk a las de wordnet
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Si no hay etiqueta, usar sustantivo como default

def apply_lemmatization(tagged_text):
    lemmatized_words = []
    for word, tag in tagged_text:
        wordnet_pos = get_wordnet_pos(tag)  # Convertir etiqueta POS al formato de WordNet
        lemmatized_word = lemmatizer.lemmatize(word, wordnet_pos)  # Aplicar lematización
        lemmatized_words.append(lemmatized_word)
    return lemmatized_words 


def preprocess_text(text, pipeline):
    text = text.lower()
    tokens = word_tokenize(text)
    
    if 'remove_punctuation' in pipeline:
        tokens = [word for word in tokens if word.isalnum()]
        print("Tokenization applied")
    
    if 'remove_stopwords' in pipeline:
        tokens = [word for word in tokens if word not in stop_words]
        print("Stopwords removed")
    
    if 'stemming' in pipeline:
        tokens = [stemmer.stem(word) for word in tokens]
        print("Stemming applied")

    if 'lemmatization' in pipeline:
        pos_tags = pos_tag(tokens)
        tokens = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tags]
        print("Lemmatization applied")

    return tokens

def preprocess_corpus(corpus, pipeline):
    return [preprocess_text(doc, pipeline) for doc in corpus]

# Example pipelines
pipeline1 = ['remove_punctuation', 'remove_stopwords', 'stemming']
pipeline2 = ['remove_punctuation', 'remove_stopwords', 'lemmatization']
pipeline3 = ['remove_stopwords', 'lemmatization']
pipeline4 = ['lemmatization']

