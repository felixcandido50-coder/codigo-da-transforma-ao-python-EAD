'''




'''

usuarios = {"admin": "1234", "joao": "senha123", "maria": "python2024"}


def fazer_login(usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login realizado com sucesso!")
    else:
        print("Usuário ou senha incorretos.")


# Exemplo de uso:
user_input = input("Digite o usuário: ")
pass_input = input("Digite a senha: ")

fazer_login(user_input, pass_input)