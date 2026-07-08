import datetime

nome = input("Digite seu nome: ")

agora = datetime.datetime.now()

print("Oi, " + nome + "! Tudo bem?")
print("Agora sao", agora.hour, "horas e", agora.minute, "minutos.")