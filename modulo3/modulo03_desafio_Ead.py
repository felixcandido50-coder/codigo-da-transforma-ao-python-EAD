'''




'''


while True:
    print("1. Soma")
    print("2. Subtração")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("Resultado:", n1 + n2)
    elif opcao == "2":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("Resultado:", n1 - n2)
    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida!")