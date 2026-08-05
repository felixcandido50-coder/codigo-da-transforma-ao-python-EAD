'''




'''

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    
    print(f"Sua média foi: {media}")
    
    if media >= 7:
        print("Status: Aprovado!")
    else:
        print("Status: Reprovado.")

# Testando a função:
calcular_media(8.0, 6.5)