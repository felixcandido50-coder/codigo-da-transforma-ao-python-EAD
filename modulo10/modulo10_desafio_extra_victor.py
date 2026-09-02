'''


'''

import tkinter as tk
from tkinter import messagebox
import requests

def buscar_filme():
    nome_filme = entry_filme.get().strip()
    if not nome_filme:
        messagebox.showwarning("Aviso", "Digite o nome de um filme.")
        return

    # Substitua 'SUA_API_KEY_AQUI' pela sua API Key ou Bearer Token do TMDB
    api_key = "SUA_API_KEY_AQUI"
    
    # 1. Busca os gêneros para mapear IDs -> Nomes
    url_generos = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=pt-BR"
    # 2. Busca do filme
    url_busca = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={nome_filme}&language=pt-BR"

    try:
        # Obter lista de gêneros
        res_gen = requests.get(url_generos, timeout=10)
        res_gen.raise_for_status()
        generos_dict = {g["id"]: g["name"] for g in res_gen.json().get("genres", [])}

        # Obter filmes
        res_filme = requests.get(url_busca, timeout=10)
        res_filme.raise_for_status()
        resultados = res_filme.json().get("results", [])

        if not resultados:
            messagebox.showinfo("Sem Resultados", "Nenhum filme foi encontrado com esse nome.")
            return

        filme = resultados[0]  # Pega o primeiro resultado da busca
        titulo = filme.get("title", "Sem título")
        sinopse = filme.get("overview", "Sinopse não disponível.")
        
        # Mapeia os IDs dos gêneros
        ids_generos = filme.get("genre_ids", [])
        lista_generos = [generos_dict.get(gid, "Outro") for gid in ids_generos]
        generos_texto = ", ".join(lista_generos) if lista_generos else "Não informado"

        # Atualiza a interface
        label_titulo.config(text=f"Título: {titulo}")
        label_genero.config(text=f"Gênero(s): {generos_texto}")
        text_sinopse.config(state="normal")
        text_sinopse.delete("1.0", tk.END)
        text_sinopse.insert(tk.END, sinopse)
        text_sinopse.config(state="disabled")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro de Conexão", f"Falha ao conectar com a API TMDB: {e}")

# Interface Gráfica
app = tk.Tk()
app.title("Buscador de Filmes - TMDB")
app.geometry("450x400")

tk.Label(app, text="Nome do Filme:", font=("Arial", 11)).pack(pady=5)
entry_filme = tk.Entry(app, font=("Arial", 11), width=30)
entry_filme.pack(pady=5)

btn_buscar = tk.Button(app, text="Buscar Filme", command=buscar_filme, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
btn_buscar.pack(pady=10)

label_titulo = tk.Label(app, text="Título: -", font=("Arial", 11, "bold"), wraplength=400, justify="left")
label_titulo.pack(anchor="w", padx=20, pady=2)

label_genero = tk.Label(app, text="Gênero(s): -", font=("Arial", 10, "italic"), wraplength=400, justify="left")
label_genero.pack(anchor="w", padx=20, pady=2)

tk.Label(app, text="Sinopse:", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=(10, 2))

text_sinopse = tk.Text(app, height=8, width=50, wrap="word", font=("Arial", 9))
text_sinopse.pack(padx=20, pady=5)
text_sinopse.config(state="disabled")

app.mainloop()