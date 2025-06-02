from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')


@app.route('/', methods=['GET'])
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



#Config Generative AI
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name='gemini-2.0-flash')

@app.route('/perguntas', methods=['GET'])
def perguntas():
    return render_template('perguntas.html')

@app.route('/responder', methods=['POST'])
def responder():
    pergunta = request.form['pergunta']
    resposta = ""

    try:
        # Envia a pergunta para o modelo Gemini
        response = model.generate_content(pergunta)
        resposta = response.text
    except Exception as e:
        resposta = f"Erro ao gerar resposta: {str(e)}"

    return render_template('perguntas.html', resposta=resposta)

@app.route('/header')
def header():
    return render_template('header.html')



app.run(debug=True)