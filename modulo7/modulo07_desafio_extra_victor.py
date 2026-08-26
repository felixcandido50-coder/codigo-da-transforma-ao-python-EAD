import sys
import types

pacote_sistema = types.ModuleType("sistema")
sys.modules["sistema"] = pacote_sistema

modulo_matematica = types.ModuleType("sistema.matematica")

def calcular_media(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

def calcular_desconto(preco, percentual):
    return preco * (1 - percentual / 100)

modulo_matematica.calcular_media = calcular_media
modulo_matematica.calcular_desconto = calcular_desconto

sys.modules["sistema.matematica"] = modulo_matematica
setattr(pacote_sistema, "matematica", modulo_matematica)

modulo_formatacao = types.ModuleType("sistema.formatacao")

def titulo(texto):
    linha = "=" * (len(texto) + 6)
    return f"{linha}\n   {texto.upper()}\n{linha}"

def moeda(valor):
    return f"R$ {valor:,.2f}".replace(".", ",")

modulo_formatacao.titulo = titulo
modulo_formatacao.moeda = moeda

sys.modules["sistema.formatacao"] = modulo_formatacao
setattr(pacote_sistema, "formatacao", modulo_formatacao)

from sistema import matematica, formatacao

def main():
    print(formatacao.titulo("Relatório do Pacote Sistema"))
    
    notas = [8.5, 9.0, 7.5, 10.0]
    media = matematica.calcular_media(notas)
    print(f"Média do aluno: {media:.2f}")
    
    preco = 250.00
    desconto = 15
    com_desconto = matematica.calcular_desconto(preco, desconto)
    
    print(f"Preço original: {formatacao.moeda(preco)}")
    print(f"Preço com {desconto}% OFF: {formatacao.moeda(com_desconto)}")

if __name__ == "__main__":
    main()