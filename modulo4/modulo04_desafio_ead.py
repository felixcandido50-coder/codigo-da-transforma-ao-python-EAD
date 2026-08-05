'''





'''


agenda = {}

while True:
    print("1. Adicionar")
    print("2. Remover")
    print("3. Buscar")
    print("4. Sair")
    
    opcao = input("Escolha: ")
    
    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        agenda[nome] = telefone
    elif opcao == "2":
        nome = input("Nome: ")
        if nome in agenda:
            del agenda[nome]
        else:
            print("Não encontrado.")
    elif opcao == "3":
        nome = input("Nome: ")
        if nome in agenda:
            print("Telefone:", agenda[nome])
        else:
            print("Não encontrado.")
    elif opcao == "4":
        break
    else:
        print("Inválido.")