import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from nltk.tokenize import sent_tokenize

# Download necessary NLTK resources
nltk.download('punkt')

def lsa_summarizer(text, num_sentences=3):
    """
    Summarize text using Latent Semantic Analysis (LSA).

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

    # Check if the TF-IDF matrix has valid dimensions
    if tfidf_matrix.shape[0] == 0:
        raise ValueError("The TF-IDF matrix is empty. Ensure the text is not empty or overly preprocessed.")

    # Step 3: Apply Truncated Singular Value Decomposition (SVD)
    svd = TruncatedSVD(n_components=1, random_state=42)
    svd.fit(tfidf_matrix)

    # Calculate sentence scores by summing term contributions for each sentence
    sentence_scores = tfidf_matrix.dot(svd.components_[0])
    print("Sentence Scores:", sentence_scores)  # Debugging line

    # Ensure we only select valid indices
    sorted_indices = np.argsort(-sentence_scores)[:num_sentences]  # Top sentences by score
    sorted_indices = sorted(sorted_indices)  # Sort indices to maintain sentence order
    print("Selected Indices:", sorted_indices)  # Debugging line

    # Step 4: Construct summary
    summary = " ".join([sentences[i] for i in sorted_indices])
    return summary


