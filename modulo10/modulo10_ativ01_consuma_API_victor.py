'''



'''

import requests

def consumir_api_clima(cidade):
    # Substitua pela sua chave de API do OpenWeatherMap
    api_key = "SUA_API_KEY_AQUI"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
    
    # Realiza a requisição à API
    response = requests.get(url)
    dados = response.json()
    
    return dados

# Teste da função
if __name__ == "__main__":
    dados_brutos = consumir_api_clima("São Paulo")
    print("Dados brutos recebidos da API:")
    print(dados_brutos)