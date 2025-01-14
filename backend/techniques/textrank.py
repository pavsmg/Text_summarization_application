
import nltk
import numpy as np
import networkx as nx
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def textrank_summarizer(text, num_sentences=3):
    """
    Summarize text using the TextRank algorithm.

    Args:
        text (str): Input text to summarize.
        num_sentences (int): Number of sentences to include in the summary.

    Returns:
        str: The summarized text.
    """
    # Step 1: Tokenize the text into sentences
    sentences = sent_tokenize(text)
    print("Sentences:", sentences)  # Debugging line

    # Ensure num_sentences does not exceed the number of sentences
    if num_sentences > len(sentences):
        num_sentences = len(sentences)

    # Step 2: Compute TF-IDF vectors for sentences
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sentences)
    print("TF-IDF Matrix Shape:", tfidf_matrix.shape)  # Debugging line

    # Step 3: Build the similarity matrix
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
    print("Similarity Matrix:", similarity_matrix)  # Debugging line

    # Step 4: Create a graph and rank sentences
    sentence_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(sentence_graph)

    # Step 5: Select top-ranked sentences
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    selected_sentences = sorted([ranked_sentences[i][1] for i in range(num_sentences)])  # Keep original order
    print("Selected Sentences:", selected_sentences)  # Debugging line

    # Step 6: Construct summary
    summary = " ".join(selected_sentences)
    return summary


