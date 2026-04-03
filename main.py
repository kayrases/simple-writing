import os
from flask import Flask, render_template, request, redirect, url_for, session
from analysis import *

app = Flask(__name__)
app.secret_key = "secret-key"

@app.route('/select_text/<filename>')
def select_text(filename):
    session["current_file"] = filename
    return redirect(url_for("welcome"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def login():
    username = request.form.get("username")
    session["username"] = username
    return redirect(url_for("welcome"))

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/signup' , methods=["POST"])
def signup():
    username = request.form.get("username")
    session["username"] = username
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")
    if password1 == password2: 
        session["username"] = username
        return redirect(url_for("welcome"))
    else: 
        return "<h1>Passwords do not match. Please try again.</h1>"
    
@app.route('/welcome' , methods=["GET"])
def welcome():
    username = session.get("username", None)
    
    if not username:
        return redirect(url_for("index"))

    filename = session.get("current_file", "white-nights.txt")
    text = load_text(filename)

    paragraphs = text.split("\n\n")
    return render_template(
        "welcome.html", 
        username=username.title(), 
        paragraphs=paragraphs
    )

@app.route('/analyze')
def analyze(): 
    filename = session.get("current_file", "white-nights.txt")
    text = load_text(filename)

    #word_count = count_words(text)
    #unique_word_count = count_unique_words(text)
    #common_words = most_common_words(text, 10)
    #histogram = word_historgram(text)

    words = clean_text(text)
    filtered_words = remove_stopwords(words)

    from collections import Counter
    freq = Counter(filtered_words)

    word_count = len(words)
    unique_word_count = len(set(words))
    common_words = freq.most_common(10)
    histogram = dict(freq.most_common(30))

    markov_text = markov_generation(words, 100)

    max_count = max(histogram.values())

    return render_template(
        "analyze.html",
        filename = filename.removesuffix(".txt").replace("-", " ").title(),
        word_count=word_count,
        unique_word_count=unique_word_count,
        common_words=common_words,
        histogram=histogram,
        max_count=max_count,
        markov_text=markov_text
    )
    
if __name__ == "__main__":
    app.run(debug=True)