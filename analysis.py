import re
import random

import nltk
from nltk.corpus import stopwords

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# read a file
def read_file(filename):
    with open(filename, "r") as file:
        return file.read()

# THIS FUNCTION SHOULD RETURN A LIST OF WORDS IN THE TEXT, INCLUDING 
# ALL LOWER CAPS, AND SHOULD NOT REMOVE ANY PUNCTUATION, BUT PUNCTUATION SHOULD BE ITS OWN ENTRY INTO THE LIST
def clean_text(text):
    text = text.lower()
    words = re.findall(r"\w+|[^\w\s]", text.lower())
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

    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]

        if word not in chain: 
            chain[word] = []
        
        chain[word].append(next_word)

    word = random.choice(words)
    result = [word]

    for _ in range(length - 1):
        if word in chain:
            word = random.choice(chain[word])
        else:
            word = random.choice(words)
        result.append(word)

    return " ".join(result)