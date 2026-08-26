# Importa módulos nativos para manipular o sistema do Python e criar módulos dinamicamente
import sys
import types

# --- CRIANDO O PACOTE "sistema" DINAMICAMENTE ---
# Cria um novo módulo em memória chamado "sistema"
pacote_sistema = types.ModuleType("sistema")
# Registra o pacote no dicionário de módulos do Python para que possa ser importado
sys.modules["sistema"] = pacote_sistema

# --- MÓDULO: sistema.matematica ---
# Cria o submódulo "matematica"
modulo_matematica = types.ModuleType("sistema.matematica")


# Função para calcular a média de uma lista de notas
def calcular_media(notas):
    if not notas:  # Evita erro de divisão por zero caso a lista esteja vazia
        return 0
    return sum(notas) / len(notas)


# Função para calcular o preço final com desconto percentual
def calcular_desconto(preco, percentual):
    return preco * (1 - percentual / 100)


# Associa as funções criadas ao submódulo de matemática
modulo_matematica.calcular_media = calcular_media
modulo_matematica.calcular_desconto = calcular_desconto

# Registra o submódulo de matemática no sistema e o vincula ao pacote "sistema"
sys.modules["sistema.matematica"] = modulo_matematica
setattr(pacote_sistema, "matematica", modulo_matematica)

# --- MÓDULO: sistema.formatacao ---
# Cria o submódulo "formatacao"
modulo_formatacao = types.ModuleType("sistema.formatacao")


# Função que cria um título emoldurado e em maiúsculas
def titulo(texto):
    linha = "=" * (len(texto) + 6)
    return f"{linha}\n   {texto.upper()}\n{linha}"


# Função para formatar números como moeda local (R$)
def moeda(valor):
    return f"R$ {valor:,.2f}".replace(".", ",")


# Associa as funções de formatação ao submódulo
modulo_formatacao.titulo = titulo
modulo_formatacao.moeda = moeda

# Registra o submódulo de formatação no sistema e o vincula ao pacote "sistema"
sys.modules["sistema.formatacao"] = modulo_formatacao
setattr(pacote_sistema, "formatacao", modulo_formatacao)

# --- USO DOS MÓDULOS CRIADOS ---
# Importa os submódulos criados dinamicamente em memória
from sistema import formatacao, matematica


# Função principal da aplicação
def main():
    # Exibe o título formatado
    print(formatacao.titulo("Relatório do Pacote Sistema"))

    # Testando o cálculo de média
    notas = [8.5, 9.0, 7.5, 10.0]
    media = matematica.calcular_media(notas)
    print(f"Média do aluno: {media:.2f}")

    # Testando o cálculo e formatação de desconto
    preco = 250.00
    desconto = 15
    com_desconto = matematica.calcular_desconto(preco, desconto)

    print(f"Preço original: {formatacao.moeda(preco)}")
    print(f"Preço com {desconto}% OFF: {formatacao.moeda(com_desconto)}")


# Garante que o código só roda se for executado diretamente (não importado)
if __name__ == "__main__":
    main()