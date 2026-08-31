'''


'''


# Atividade 2: Criando e usando uma exceção personalizada

# Definindo a exceção personalizada
class SaldoInsuficienteError(Exception):
    pass

# Simulação da conta bancária
saldo = 500.0

try:
    valor_saque = float(input(f"Seu saldo atual é R${saldo:.2f}. Quanto deseja sacar? "))
    
    if valor_saque > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque!")
    elif valor_saque <= 0:
        print("Valor de saque inválido!")
    else:
        saldo -= valor_saque
        print(f"Saque realizado com sucesso! Saldo restante: R${saldo:.2f}")

except SaldoInsuficienteError as erro:
    print(f"Erro no saque: {erro}")
except ValueError:
    print("Erro: Digite um valor numérico válido!")