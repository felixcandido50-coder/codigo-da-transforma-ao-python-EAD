'''


'''

import tkinter as tk
from tkinter import messagebox
import requests

def buscar_clima_com_tratamento():
    cidade = entry_cidade.get().strip()
    if not cidade:
        messagebox.showwarning("Aviso", "Por favor, digite o nome de uma cidade.")
        return

    api_key = "SUA_API_KEY_AQUI"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"

    # Bloco try-except para tratamento de erros
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Verifica erros HTTP (4xx, 5xx)
        
        dados = response.json()
        temp = dados["main"]["temp"]
        condicao = dados["weather"][0]["description"].capitalize()

        label_resultado.config(text=f"Temperatura: {temp}°C\nCondição: {condicao}")

    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            messagebox.showerror("Erro 404", "Cidade não encontrada. Verifique o nome digitado.")
        else:
            messagebox.showerror("Erro HTTP", f"Falha na requisição. Código: {response.status_code}")
            
    except requests.exceptions.Timeout:
        messagebox.showerror("Erro de Conexão", "A requisição demorou muito para responder (Timeout).")
        
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro de Conexão", f"Falha na conexão com a rede: {e}")

# Interface Gráfica Tkinter
app = tk.Tk()
app.title("Atividade 3 - Tratamento de Erros")
app.geometry("320x220")

tk.Label(app, text="Cidade:").pack(pady=5)
entry_cidade = tk.Entry(app)
entry_cidade.pack(pady=5)

btn_buscar = tk.Button(app, text="Buscar com Segurança", command=buscar_clima_com_tratamento)
btn_buscar.pack(pady=5)

label_resultado = tk.Label(app, text="", justify="left")
label_resultado.pack(pady=10)

app.mainloop()