import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret-key"  
acts = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    session["username"] = username
    return redirect(url_for("welcome"))

@app.route('/login', methods=['POST'])
def register():
    return redirect(url_for("register"))

@app.route('/register', methods=['POST'])
def signup():
    username = request.form.get("username")
    session["username"] = username
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")
    if password1 == password2: 
        return render_template("index.html")
    else: 
        return "<h1>Passwords do not match. Please try again.</h1>"
    
@app.route('/welcome')
def welcome():
    username = session.get("username", None)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'data', 'white-nights.txt')

    with open(file_path, "r", encoding="utf-8") as file: 
        text = file.read()

    return render_template("welcome.html", username=username.title(), text=text)

@app.route('/act')
def addact():
    actname = session.get("act", None)
    acts.append(actname)
    return render_template('act.html')

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