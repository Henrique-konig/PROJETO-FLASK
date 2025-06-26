from app import app
from flask import render_template

@app.route('/')
def homepage():
    nome = "Henrique"
    idade = 17
    interesses = ["Python", "Flask", "JavaScript"]
    return render_template('index.html', nome=nome, idade=idade, interesses=interesses)

@app.route('/sobre/')
def sobre():
    return render_template('sobre.html')

