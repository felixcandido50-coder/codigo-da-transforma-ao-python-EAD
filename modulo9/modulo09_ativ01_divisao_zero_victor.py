'''


'''


# Atividade 1: Uso de try-except para tratar erros em uma calculadora

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")

except ZeroDivisionError:
    print("Erro: Não é possível dividir um número por zero!")
except ValueError:
    print("Erro: Por favor, digite apenas números válidos!")