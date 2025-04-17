HEAD
from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message")
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é uma IA amigável e útil."},
                {"role": "user", "content": user_input}
            ]
        )
        return jsonify({"response": response.choices[0].message["content"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import openai
import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Rota para servir o index.html
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

# Rota para processar perguntas
@app.route('/perguntar', methods=['POST'])
def perguntar():
    data = request.get_json()
    pergunta = data.get('pergunta')

    openai.api_key = os.getenv("OPENAI_API_KEY")

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": pergunta}]
    )

    return jsonify({'resposta': resposta.choices[0].message['content']})
 ac2e84f6a50c06b829b59961ca691521c312927e
