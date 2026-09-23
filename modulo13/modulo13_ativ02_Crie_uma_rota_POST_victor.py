'''




'''

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    dados = request.get_json()
    
    if not dados or 'nome' not in dados or 'email' not in dados:
        return jsonify({"erro": "Dados inválidos. Envie 'nome' e 'email'."}), 400
    
    nome = dados['nome']
    email = dados['email']
    
    return jsonify({
        "mensagem": "Usuário recebido com sucesso!",
        "usuario": {
            "nome": nome,
            "email": email
        }
    }), 201

if __name__ == '__main__':
    app.run(debug=True)