'''


'''

class carro:
    def __int__(self,marca, modelo):
        self.marca  = marca
        self.modelo = modelo

    def  exebir_info(self):
        return f"marca: {self.marca}, modelo:{self.modelo}"

meu_carro = carro("ford", "mustang")
print(meu_carro.exibir_info())       # Classe pai
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print("Marca:", self.marca, "- Modelo:", self.modelo)


# Classe filho (herda de Carro)
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        print("Marca:", self.marca, "- Modelo:", self.modelo, "- Bateria:", self.autonomia_bateria, "km")



c1 = Carro("Fiat", "Uno")
c1.exibir_info()

c2 = CarroEletrico("Tesla", "Model S", 400)
c2.exibir_info()