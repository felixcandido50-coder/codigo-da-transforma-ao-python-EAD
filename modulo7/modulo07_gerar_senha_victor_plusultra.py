'''
A Tabela ASCII (American Standard Code for Information Interchange, ou Código Padrão Americano para o Intercâmbio de Informações) é um sistema de codificação que traduz letras, números, símbolos e comandos para a linguagem que o computador entende: os números.

A tabela hexadecimal (ou sistema hexadecimal) é uma forma de representar valores numéricos utilizando a base 16. Enquanto o nosso sistema do dia a dia é o decimal (base 10, com dígitos de 0 a 9), o sistema hexadecimal utiliza 16 símbolos para representar números.


'''

import random
import string
import tkinter as tk
from tkinter import messagebox

# ==========================================
# 🎨 PALETA DE CORES DEFINIDA
# ==========================================
COLOR_AZUL_ESC = "#040709"  # Fundo principal
COLOR_AZUL_MED = "#1d2326"  # Bordas e detalhes
COLOR_AZUL_CLA = "#3C673C"  # Destaque do texto da senha
COLOR_VERDE = "#150808"     # Botão Principal (Gerar)
COLOR_ROSA = "#b83764"      # Alertas / Erros
COLOR_AMARELO = "#282723"   # Botão Copiar
COLOR_ACO = "#262c5a"       # Fundo dos campos e cards
COLOR_TEXTO = "#ffffff"     # Texto geral em branco para bom contraste


# ==========================================
# ⚙️ LÓGICA DO PROGRAMA
# ==========================================
def gerar_senha():
    try:
        # Pega o valor digitado no campo de tamanho
        tamanho = int(entry_tamanho.get())
        
        if tamanho <= 0:
            messagebox.showwarning("Atenção", "O tamanho da senha deve ser maior que zero!")
            return

        # Lógica de geração de senha
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

        # Atualiza o campo de resultado da senha
        entry_resultado.config(state="normal") # Libera para escrita
        entry_resultado.delete(0, tk.END)      # Limpa texto antigo
        entry_resultado.insert(0, senha)       # Insere a nova senha
        entry_resultado.config(state="readonly")# Bloqueia para edição manual
        
    except ValueError:
        # Trata erros caso o usuário digite letras no campo de tamanho
        messagebox.showerror("Erro de Entrada", "Por favor, insira um número inteiro válido!")

def copiar_senha():
    senha = entry_resultado.get()
    if senha:
        # Limpa a área de transferência do sistema e adiciona a nova senha
        janela.clipboard_clear()
        janela.clipboard_append(senha)
        messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência!")
    else:
        messagebox.showwarning("Aviso", "Gere uma senha primeiro antes de copiar!")


# ==========================================
# 🖥️ CONSTRUÇÃO DA INTERFACE (GUI)
# ==========================================
janela = tk.Tk()
janela.title("Gerador de Senhas Seguras")
janela.geometry("400x320")
janela.configure(bg=COLOR_AZUL_ESC)
janela.resizable(False, False)

# --- Título ---
lbl_titulo = tk.Label(
    janela, 
    text="Gerador de Senhas", 
    font=("Arial", 16, "bold"), 
    bg=COLOR_AZUL_ESC, 
    fg=COLOR_AZUL_CLA
)
lbl_titulo.pack(pady=15)

# --- Frame Central (Card) ---
frame_card = tk.Frame(janela, bg=COLOR_ACO, bd=2, relief="flat", padx=15, pady=15)
frame_card.pack(pady=5, fill="x", padx=20)

# --- Campo: Tamanho da Senha ---
lbl_tamanho = tk.Label(
    frame_card, 
    text="Tamanho da Senha:", 
    font=("Arial", 10, "bold"), 
    bg=COLOR_ACO, 
    fg=COLOR_TEXTO
)
lbl_tamanho.grid(row=0, column=0, sticky="w", pady=5)

entry_tamanho = tk.Entry(
    frame_card, 
    font=("Arial", 10), 
    width=8, 
    bg=COLOR_AZUL_ESC, 
    fg=COLOR_TEXTO, 
    insertbackground="white",
    bd=1,
    relief="solid"
)
entry_tamanho.insert(0, "12")  # Valor padrão: 12
entry_tamanho.grid(row=0, column=1, sticky="e", pady=5)

# --- Campo: Exibição da Senha Gerada ---
entry_resultado = tk.Entry(
    frame_card, 
    font=("Consolas", 12, "bold"), 
    width=25, 
    bg=COLOR_AZUL_ESC, 
    fg=COLOR_AZUL_CLA, 
    bd=1, 
    relief="solid", 
    justify="center",
    state="readonly"
)
entry_resultado.grid(row=1, column=0, columnspan=2, pady=12)

# --- Botão: Gerar Senha ---
btn_gerar = tk.Button(
    janela, 
    text="Gerar Senha", 
    font=("Arial", 11, "bold"), 
    bg=COLOR_VERDE, 
    fg="#000000", 
    activebackground=COLOR_AZUL_MED,
    bd=0, 
    padx=10, 
    pady=5, 
    cursor="hand2",
    command=gerar_senha
)
btn_gerar.pack(pady=10)

# --- Botão: Copiar Senha ---
btn_copiar = tk.Button(
    janela, 
    text="Copiar Senha", 
    font=("Arial", 10, "bold"), 
    bg=COLOR_AMARELO, 
    fg="#000000", 
    activebackground=COLOR_ROSA,
    bd=0, 
    padx=8, 
    pady=3, 
    cursor="hand2",
    command=copiar_senha
)
btn_copiar.pack(pady=2)

# --- Loop Principal ---
if __name__ == "__main__":
    janela.mainloop()