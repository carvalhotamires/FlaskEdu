from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')

@app.route('/dicionario')
def dicionario():
    return render_template('dicionario.html')

@app.route('/fundamentos')
def fundamentos():
    return render_template('fundamentos.html')

@app.route('/perguntas')
def perguntas():
    return render_template('perguntas.html')

@app.route('/header')
def header():
    return render_template('header.html')

app.run()