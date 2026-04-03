import re
import random
import os

import nltk
from nltk.corpus import stopwords

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

def load_text(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'data', filename)
    with open(file_path, "r", encoding="utf-8") as file: 
        text = file.read()
    return text

# read a file
def read_file(filename):
    with open(filename, "r") as file:
        return file.read()

def clean_text(text):
    text = text.lower()
    words = re.findall(r"\.\.\.|\-\-|\b\w+(?:'\w+)?\b|[.,!?;:\"()\[\]{}\-]", text)
    return words

def clean_text_no_punctuation(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text

stop_words = set(stopwords.words('english'))
def remove_stopwords(words):
    filtered_words = [word for word in words if word not in stop_words and word.isalpha()]
    return filtered_words

# generate a new text of a given length using a Markov chain based on the input text
def markov_generation(words, length=100):

    chain = {}

    # create a dictionary of words that have followed after each other
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]

        if word not in chain: 
            chain[word] = []
        chain[word].append(next_word)

    # start the generated text with a random word
    isPunctuation = True
    while isPunctuation:
        word = random.choice(words)
        # the first character of word should be a character, not punctuation
        if word[0].isalpha():
            isPunctuation = False
            result = [word]

    for _ in range(length - 1):
        if word in chain:
            word = random.choice(chain[word])
        else:
            word = random.choice(words)
        result.append(word)

    punctuation = set(".!?;:\"()[]{}-")
    text = ""
    for token in result: 
        if token in punctuation or token in ["...", "--"]:
            text+= token
        elif text == "":
            text+= token
        else:
            text+= " " + token

    return text