'''


'''


# Desafio Extra: Sistema de login com tratamento de erros e limite de tentativas

usuario_correto = "admin"
senha_correta = "1234"
tentativas = 3

print("=== SISTEMA DE LOGIN ===")

while tentativas > 0:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    
    try:
        if usuario == usuario_correto and senha == senha_correta:
            print("\nLogin realizado com sucesso! Bem-vindo!")
            break
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f"Usuário ou senha incorretos. Tentativas restantes: {tentativas}\n")
            else:
                raise Exception("Número máximo de tentativas excedido. Acesso bloqueado!")

    except Exception as erro:
        print(f"\nErro de Acesso: {erro}")