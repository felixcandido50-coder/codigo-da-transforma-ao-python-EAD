'''




'''


lista = []

while True:
    print("1. Adicionar")
    print("2. Remover")
    print("3. Ver")
    print("4. Sair")
    
    opcao = input("Escolha: ")
    
    if opcao == "1":
        item = input("Item: ")
        lista.append(item)
    elif opcao == "2":
        item = input("Item: ")
        if item in lista:
            lista.remove(item)
        else:
            print("Não encontrado.")
    elif opcao == "3":
        print("Lista:", lista)
    elif opcao == "4":
        break
    else:
        print("Inválido.")