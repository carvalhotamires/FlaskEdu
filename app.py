from flask import Flask, render_template
from dicionariodetermos import bd_termos, adicionar_termos, deletar_termo, visualizar_termos, alterar_termo, salvar_termos
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')

@app.route('/dicionario')
def dicionario():
    visualizar_termos(bd_termos)  # Só para fins de log
    return render_template('dicionario.html', termos=bd_termos)

@app.route('/fundamentos')
def fundamentos():
    return render_template('fundamentos.html')

@app.route('/perguntas')
def perguntas():
    return render_template('perguntas.html')

app.run(debug=True)