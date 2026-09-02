'''



'''


import tkinter as tk
from tkinter import messagebox
import requests

def buscar_e_exibir_clima():
    cidade = entry_cidade.get().strip()
    if not cidade:
        messagebox.showwarning("Aviso", "Digite o nome de uma cidade.")
        return

    api_key = "SUA_API_KEY_AQUI"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"

    response = requests.get(url)
    dados = response.json()

    # Filtro das informações específicas
    temp = dados["main"]["temp"]
    condicao = dados["weather"][0]["description"].capitalize()
    umidade = dados["main"]["humidity"]

    # Exibição organizada na interface
    texto_formatado = f"Cidade: {dados['name']}\nTemperatura: {temp}°C\nCondição: {condicao}\nUmidade: {umidade}%"
    label_resultado.config(text=texto_formatado)

# Interface Gráfica Tkinter
app = tk.Tk()
app.title("Atividade 2 - Exibir Clima")
app.geometry("300x200")

tk.Label(app, text="Cidade:").pack(pady=5)
entry_cidade = tk.Entry(app)
entry_cidade.pack(pady=5)

btn_buscar = tk.Button(app, text="Buscar", command=buscar_e_exibir_clima)
btn_buscar.pack(pady=5)

label_resultado = tk.Label(app, text="", justify="left")
label_resultado.pack(pady=10)

app.mainloop()