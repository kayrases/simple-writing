import re
import random
import os

import nltk
from nltk.corpus import stopwords

import json

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

    # TODO: keep proper nouns capital

    text = text.lower()
    text = text.replace("’", "'").replace("‘", "'")
    words = re.findall(r"[\d+\]|\.\.\.|\-\-|\b[a-z0-9]+(?:'[a-z]+)?\b|[.,!?;:()\[\]{}\-]", text)
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

def create_chain(words):
    chain = {}
    # create a dictionary of words that have followed after each other
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]

        if word not in chain: 
            chain[word] = []
        chain[word].append(next_word)
    return chain

def save_chain(chain, filename="chain.json"):
    with open(filename, "w") as f:
        json.dump(chain, f)

def load_chain(filename="chain.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}

# generate a new text of a given length using a Markov chain based on the input text
def markov_generation(words, chain, length=100):
    if not chain:
        return ""

    # start the generated text with a random word
    isPunctuation = True
    while isPunctuation:
        word = random.choice(words)
        # the first character of word should be a character, not punctuation
        if word[0].isalpha():
            isPunctuation = False
            result = [word]

    for _ in range(length - 1):
        if word in chain and chain[word]:
            word = random.choice(chain[word])
        else:
            word = random.choice(words)
        result.append(word)

    endSetnence = set(".!?")
    punctuation = set(",;:()[]{}-\"''")
    text = ""
    capitalize = True
    for token in result: 
        if token in punctuation or token in ["...", "--"]:
            text += token
        elif token in endSetnence:
            text += token
            capitalize = True
        elif text == "" and capitalize:
            text+= token.capitalize()
            capitalize = False
        elif capitalize:
            text+= " " + token.capitalize()
            capitalize = False
        else: 
            text+= " " + token

    return text

def get_feedback(generated_text):
    good = True

    # if the user clicks a button for bad, set good to false

    return good

# reinforcment learning based on if the user gives a positive or negative response
def reinforce_chain(chain, generated_text, good):
    words = clean_text(generated_text)

    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]

        if word not in chain:
            chain[word] = []

        if good:
            # add one instance of the next word
            chain[word].append(next_word)
            
        else:
            # remove one instance of the next word
            if next_word in chain[word]:
                chain[word].remove(next_word)
                if not chain[word]:
                    del chain[word]

    return chain