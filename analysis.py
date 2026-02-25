import re

def read_file(filename):
    # read a file
    return ""

def count_words(text):
    # count the number of words in a text
    return ""

def word_historgram(text):
    # create a histogram of word frequencies
    return ""

def most_common_words(text):
    # find the most common words in a text
    return ""

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text

def analyze_text(text):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    word_count = len(words)
    unique_words = set(words)
    unique_word_count = len(unique_words)
    return {
        "word_count": len(words),
        "unique_word_count": len(set(words))
    }