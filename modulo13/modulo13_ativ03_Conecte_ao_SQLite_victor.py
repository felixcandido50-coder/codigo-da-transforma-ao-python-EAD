'''




'''

import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Função para inicializar a base de dados
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    dados = request.get_json()
    
    if not dados or 'nome' not in dados or 'email' not in dados:
        return jsonify({"erro": "Parâmetros 'nome' e 'email' são obrigatórios."}), 400

    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (dados['nome'], dados['email']))
        conn.commit()
        usuario_id = cursor.lastrowid
        conn.close()

        return jsonify({
            "mensagem": "Usuário gravado na base de dados com sucesso!",
            "id": usuario_id,
            "nome": dados['nome'],
            "email": dados['email']
        }), 201

    except sqlite3.IntegrityError:
        return jsonify({"erro": "Email já cadastrado."}), 400
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)