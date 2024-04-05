from flask import Flask, render_template, request, jsonify
import time
import json
lista_de_requisicoes = []
app = Flask(__name__)

@app.route('/dash', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/ping', methods=['GET'])
def ping():
    lista_de_requisicoes.append((f"Data e Hora: {time.ctime()}", "Requisicao PING"))
    return jsonify({"resposta": "pong"})

@app.route('/echo', methods=['POST'])
def echo():
    lista_de_requisicoes.append((f"Data e Hora: {time.ctime()}", "Requisicao ECHO"))
    data = request.get_json()
    return jsonify(data)

@app.route('/info', methods=['GET'])
def info():
    lista_de_requisicoes.append((f"Data e Hora: {time.ctime()}", "requisicao INFO"))
    htmlParagraph = "<p> </p>".join([f"{i[0]} - {i[1]}" for i in lista_de_requisicoes])
    return htmlParagraph
if __name__ == '__main__':
    app.run(debug=True)