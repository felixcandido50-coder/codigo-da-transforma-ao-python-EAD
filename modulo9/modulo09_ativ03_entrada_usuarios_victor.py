'''


'''


# Atividade 3: Validando se a idade digitada é um número positivo

try:
    idade = int(input("Digite a sua idade: "))
    
    if idade <= 0:
        print("Erro: A idade deve ser um número positivo e maior que zero!")
    else:
        print(f"Idade cadastrada com sucesso: {idade} anos.")

except ValueError:
    print("Erro: Você deve digitar um número inteiro válido para a idade!")