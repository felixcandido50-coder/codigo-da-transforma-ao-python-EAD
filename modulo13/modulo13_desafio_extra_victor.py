import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuração e criação simples das tabelas
def init_db():
    conn = sqlite3.connect('blog_simples.db')
    cursor = conn.cursor()
    
    # Tabela de Usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')
    
    # Tabela de Posts
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL,
            usuario_id INTEGER
        )
    ''')
    
    # Tabela de Comentários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comentarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT NOT NULL,
            post_id INTEGER,
            usuario_id INTEGER
        )
    ''')
    
    conn.commit()
    conn.close()

init_db()

# 1. AUTENTICAÇÃO / USUÁRIOS
@app.route('/cadastrar-usuario', methods=['POST'])
def cadastrar_usuario():
    dados = request.get_json()
    
    conn = sqlite3.connect('blog_simples.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (dados['nome'],))
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    
    return jsonify({"mensagem": "Usuário criado com sucesso!", "usuario_id": user_id}), 201


# 2. GERENCIAMENTO DE POSTS
@app.route('/posts', methods=['POST'])
def criar_post():
    dados = request.get_json()
    
    conn = sqlite3.connect('blog_simples.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (titulo, conteudo, usuario_id) VALUES (?, ?, ?)", 
                   (dados['titulo'], dados['conteudo'], dados['usuario_id']))
    conn.commit()
    post_id = cursor.lastrowid
    conn.close()
    
    return jsonify({"mensagem": "Post publicado!", "post_id": post_id}), 201

@app.route('/posts', methods=['GET'])
def listar_posts():
    conn = sqlite3.connect('blog_simples.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, conteudo, usuario_id FROM posts")
    posts = cursor.fetchall()
    conn.close()
    
    resultado = []
    for p in posts:
        resultado.append({"id": p[0], "titulo": p[1], "conteudo": p[2], "autor_id": p[3]})
        
    return jsonify(resultado), 200


# 3. GERENCIAMENTO DE COMENTÁRIOS
@app.route('/comentarios', methods=['POST'])
def criar_comentario():
    dados = request.get_json()
    
    conn = sqlite3.connect('blog_simples.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO comentarios (texto, post_id, usuario_id) VALUES (?, ?, ?)", 
                   (dados['texto'], dados['post_id'], dados['usuario_id']))
    conn.commit()
    conn.close()
    
    return jsonify({"mensagem": "Comentário adicionado!"}), 201

@app.route('/posts/<int:post_id>/comentarios', methods=['GET'])
def listar_comentarios(post_id):
    conn = sqlite3.connect('blog_simples.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, texto, usuario_id FROM comentarios WHERE post_id = ?", (post_id,))
    comentarios = cursor.fetchall()
    conn.close()
    
    resultado = []
    for c in comentarios:
        resultado.append({"id": c[0], "texto": c[1], "autor_id": c[2]})
        
    return jsonify(resultado), 200

from waitress import serve

if __name__ == '__main__':
    serve(app, host='127.0.0.1', port=5000)