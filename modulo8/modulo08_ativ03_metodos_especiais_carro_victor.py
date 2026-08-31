'''


'''

class Carro:
    # __init__ serve para criar o objeto com os atributos
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # __str__ serve para definir o texto que aparece no print()
    def __str__(self):
        return f"Carro: {self.marca} {self.modelo}"


# Teste
meu_carro = Carro("Chevrolet", "Onix")

# O print chama o __str__ automaticamente
print(meu_carro)