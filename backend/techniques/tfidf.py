from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords_tfidf(processed_corpus, top_n=15):
    """
    Extrae palabras clave utilizando TF-IDF.
    Args:
        processed_corpus (list of list of str): Corpus tokenizado.
        top_n (int): Número de palabras clave a extraer por documento.
    Returns:
        list of dict: Palabras clave para cada documento.
    """
    processed_texts = [' '.join(doc_tokens) for doc_tokens in processed_corpus]
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(processed_texts)
    feature_names = tfidf_vectorizer.get_feature_names_out()

    keywords_per_doc = []

    for doc_idx in range(tfidf_matrix.shape[0]):
        tfidf_vector = tfidf_matrix[doc_idx]
        tfidf_scores = tfidf_vector.toarray().flatten()
        top_indices = tfidf_scores.argsort()[::-1][:top_n]
        top_words = [feature_names[i] for i in top_indices]
        keywords_per_doc.append({"doc_index": doc_idx, "keywords": top_words})

    return keywords_per_doc
