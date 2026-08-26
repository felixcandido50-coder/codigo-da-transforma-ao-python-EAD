import random
import math

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

print("=== JOGO DA ADIVINHAÇÃO ===")
print("Tente adivinhar o número secreto entre 1 e 100!")

while not acertou:
    palpite = int(input("Digite o seu palpite: "))
    tentativas += 1
    
    # Calculando a diferença absoluta usando math.abs (fabs)
    diferenca = math.fabs(numero_secreto - palpite)
    
    if palpite == numero_secreto:
        print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s)!")
        acertou = True
    elif palpite < numero_secreto:
        print(f"O número é MAIOR. (Dica: você errou por {int(diferenca)})")
    else:
        print(f"O número é MENOR. (Dica: você errou por {int(diferenca)})")