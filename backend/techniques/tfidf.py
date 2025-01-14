import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Download NLTK resources
nltk.download('punkt')

def tfidf_summarizer(text, num_sentences=3):
    """
    Summarize text using TF-IDF.

    Args:
        text (str): Input text to summarize.
        num_sentences (int): Number of sentences to include in the summary.

    Returns:
        str: The summarized text.
    """
    # Step 1: Split the text into sentences
    sentences = sent_tokenize(text)
    print("Sentences:", sentences)  # Debugging line

    # Ensure num_sentences does not exceed the number of sentences
    if num_sentences > len(sentences):
        num_sentences = len(sentences)

    # Step 2: Compute TF-IDF matrix
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sentences)
    print("TF-IDF Matrix Shape:", tfidf_matrix.shape)  # Debugging line

    # Step 3: Compute sentence scores by summing TF-IDF values for each sentence
    sentence_scores = np.array(tfidf_matrix.sum(axis=1)).flatten()
    print("Sentence Scores:", sentence_scores)  # Debugging line

    # Step 4: Select top-ranked sentences
    sorted_indices = np.argsort(-sentence_scores)[:num_sentences]  # Top `num_sentences` indices
    sorted_indices = sorted(sorted_indices)  # Sort indices to preserve sentence order
    print("Selected Indices:", sorted_indices)  # Debugging line

    # Step 5: Construct summary
    summary = " ".join([sentences[i] for i in sorted_indices])
    return summary


