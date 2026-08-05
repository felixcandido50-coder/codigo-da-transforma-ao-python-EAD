'''


'''

class carro:
    def __int__(self,marca, modelo):
        self.marca  = marca
        self.modelo = modelo

    def  exebir_info(self):
        return f"marca: {self.marca}, modelo:{self.modelo}"

meu_carro = carro("ford", "mustang")
print(meu_carro.exibir_info())       