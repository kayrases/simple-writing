import os
from flask import Flask, render_template, request, redirect, url_for, session
from analysis import *

app = Flask(__name__)
app.secret_key = "secret-key"  
acts = []

# load in white nights text
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'data', 'white-nights.txt')
with open(file_path, "r", encoding="utf-8") as file: 
    text = file.read()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def login():
    username = request.form.get("username")
    session["username"] = username
    return redirect(url_for("welcome"))

''' TODO: change the route that this starts from. It can't also start from /login''' 

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

    paragraphs = text.split("\n\n")
    return render_template("welcome.html", username=username.title(), paragraphs=paragraphs)

@app.route('/analyze')
def analyze(): 
    word_count = count_words(text)
    unique_word_count = count_unique_words(text)
    common_words = most_common_words(text, 10)
    histogram = word_historgram(text)
    markov_text = markov_generation(text, 100)

    return render_template(
        "analyze.html",
        word_count=word_count,
        unique_word_count=unique_word_count,
        common_words=common_words,
        histogram=histogram,
        markov_text=markov_text
    )

'''
@app.route('/act')
def addact():
    actname = session.get("act", None)
    acts.append(actname)
    return render_template('act.html')
'''

'''
@app.route('/populateacts')
def populateacts():
    populated = ""
    for act in acts:
        populated += f'<button class="{button}" onclick="{act}.href="actone/actone.html"">{act}</button>'
    return populated
'''
    
if __name__ == "__main__":
    app.run(debug=True)