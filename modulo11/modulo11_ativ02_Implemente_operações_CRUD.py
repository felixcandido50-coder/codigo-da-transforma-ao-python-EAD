'''




'''

import sqlite3

conexao = sqlite3.connect("sistema.db")
cursor = conexao.cursor()

# 1. INSERIR
cursor.execute(
    "INSERT INTO Clientes (nome, email) VALUES (?, ?)",
    ("Ana Silva", "ana@email.com"),
)
cursor.execute(
    "INSERT INTO Clientes (nome, email) VALUES (?, ?)",
    ("Bruno Costa", "bruno@email.com"),
)
conexao.commit()
print("Clientes inseridos!")

# 2. CONSULTAR
print("\n--- Lista de Clientes ---")
cursor.execute("SELECT * FROM Clientes")
clientes = cursor.fetchall()
for c in clientes:
    print(c)

# 3. ATUALIZAR
cursor.execute(
    "UPDATE Clientes SET email = ? WHERE id = ?", ("ana.silva@email.com", 1)
)
conexao.commit()
print("\nE-mail da Ana atualizado!")

# 4. DELETAR
cursor.execute("DELETE FROM Clientes WHERE id = ?", (2,))
conexao.commit()
print("Cliente com ID 2 deletado!")

conexao.close()