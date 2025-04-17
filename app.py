from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv  # Importando o dotenv

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Carregar as variáveis do arquivo .env
load_dotenv()

# Rota para servir o index.html
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

# Rota para processar perguntas
@app.route('/perguntar', methods=['POST'])
def perguntar():
    data = request.get_json()
    pergunta = data.get('pergunta')

    openai.api_key = os.getenv("OPENAI_API_KEY")  # Usando a chave da API do .env

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": pergunta}]
    )

    return jsonify({'resposta': resposta.choices[0].message['content']})

if __name__ == "__main__":
    app.run(debug=True)
