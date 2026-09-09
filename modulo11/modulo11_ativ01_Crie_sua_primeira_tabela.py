'''




'''

import sqlite3

# Conecta ao banco de dados (cria o arquivo se não existir)
conexao = sqlite3.connect("sistema.db")
cursor = conexao.cursor()

# Cria a tabela Clientes
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
"""
)

# Salva as alterações e fecha
conexao.commit()
conexao.close()

print("Banco de dados e tabela Clientes criados com sucesso!")