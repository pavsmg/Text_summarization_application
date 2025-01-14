from transformers import pipeline

def split_text(text, max_tokens=500):
    sentences = text.split('. ')
    chunks = []
    current_chunk = []
    current_length = 0
    for sentence in sentences:
        tokens = len(sentence.split())
        if current_length + tokens <= max_tokens:
            current_chunk.append(sentence)
            current_length += tokens
        else:
            chunks.append(". ".join(current_chunk))
            current_chunk = [sentence]
            current_length = tokens
    if current_chunk:
        chunks.append(". ".join(current_chunk))
    return chunks


def summarize_with_bert(text, max_length=130, min_length=60):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

def summarize_text_complete(text):
    chunks = split_text(text)
    summaries = [summarize_with_bert(chunk) for chunk in chunks]
    full_summary = " ".join(summaries)
    return full_summary

