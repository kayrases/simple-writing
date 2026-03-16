import re
import random

# read a file
def read_file(filename):
    with open(filename, "r") as file:
        return file.read()
    
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text

# count the number of words in a text
def count_words(text):
    cleaned = clean_text(text)
    words = cleaned.split()
    return len(words)

# count the number of unique words in a text
def count_unique_words(text):
    cleaned = clean_text(text)
    words=cleaned.split()
    return len(set(words))

# find the most common num words in a text
def most_common_words(text, num=10):
    cleaned = clean_text(text)
    words = cleaned.split()

    freq = {}
    for word in words: 
        if word in freq:
            freq[word] += 1
        else: 
            freq[word] = 1
    
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:num]

# create a histogram of top 30 word frequencies
def word_historgram(text):
    # call most_common_words to get the top 30 words and their frequencies
    most_common = most_common_words(text, 30)

    histogram = {}
    for word, count in most_common:
        histogram[word] = count
    
    return histogram

# generate a new text of a given length using a Markov chain based on the input text
def markov_generation(text, length=100):
    cleaned = clean_text(text)
    words = cleaned.split()

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

'''
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
'''