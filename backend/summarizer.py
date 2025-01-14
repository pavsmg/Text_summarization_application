from techniques.lsa import lsa_summarizer
from techniques.tfidf import tfidf_summarizer
from techniques.textrank import textrank_summarizer
from techniques.transformer import summarize_text_complete
from techniques.word_freq import word_frequency_summarizer

def summarizer(text, technique, num_sentences=3):
    """
    Summarize text using the specified technique.

    Args:
        text (str): Input text to summarize.
        technique (str): Summarization technique to use.
        num_sentences (int): Number of sentences to include in the summary.

    Returns:
        str: The summarized text.
    """
    if technique == "LSA":
        return lsa_summarizer(text, num_sentences)
    elif technique == "TF-IDF":
        return tfidf_summarizer(text, num_sentences)
    elif technique == "TextRank":
        return textrank_summarizer(text, num_sentences)
    elif technique == "BERT":
        return summarize_text_complete(text)
    elif technique == "WordFreq":
        return word_frequency_summarizer(text, num_sentences)
    else:
        return "Técnica de resumen no válida"