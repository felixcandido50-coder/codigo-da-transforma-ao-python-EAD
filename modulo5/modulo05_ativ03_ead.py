'''




'''

def maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor


# Exemplo de uso:
numeros = [12, 5, 8, 25, 3]
maior, menor = maior_menor(numeros)

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")