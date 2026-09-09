'''



'''

import sqlite3


# Função para criar o banco de dados e a tabela de tarefas
def criar_tabela():
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """
    )
    conexao.commit()
    conexao.close()


# Função para adicionar uma nova tarefa
def adicionar_tarefa(descricao):
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO tarefas (descricao, status) VALUES (?, ?)",
        (descricao, "Pendente"),
    )
    conexao.commit()
    conexao.close()
    print(f"Tarefa '{descricao}' adicionada com sucesso!")


# Função para listar todas as tarefas
def visualizar_tarefas():
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conexao.close()

    print("\n--- MINHAS TAREFAS ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for t in tarefas:
            print(f"ID: {t[0]} | Descrição: {t[1]} | Status: {t[2]}")
    print("----------------------\n")


# Função para excluir uma tarefa pelo ID
def excluir_tarefa(id_tarefa):
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conexao.commit()
    conexao.close()
    print(f"Tarefa ID {id_tarefa} excluída com sucesso!")


# --- TESTANDO O SISTEMA ---

# 1. Cria a tabela
criar_tabela()

# 2. Adiciona tarefas de teste
adicionar_tarefa("Estudar Python para a prova")
adicionar_tarefa("Fazer os exercícios de SQL")
adicionar_tarefa("Entregar a atividade no AVA")

# 3. Visualiza a lista
visualizar_tarefas()

# 4. Exclui a segunda tarefa (ID 2)
excluir_tarefa(2)

# 5. Visualiza novamente para conferir o resultado
visualizar_tarefas()