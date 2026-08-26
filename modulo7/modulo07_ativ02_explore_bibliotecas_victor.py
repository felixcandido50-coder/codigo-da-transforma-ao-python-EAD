from datetime import date


data_atual = date.today()

fim_do_ano = date(data_atual.year, 12, 31)

dias_restantes = (fim_do_ano - data_atual).days

print("--- Calculadora de Dias para o Fim do Ano ---")
print(f"Data de hoje: {data_atual.strftime('%d/%m/%Y')}")
print(f"Faltam {dias_restantes} dias para o ano acabar!")# Importa a classe 'date' do módulo nativo 'datetime' do Python
from datetime import date

# Obtém a data atual do sistema (Ano, Mês, Dia)
data_atual = date.today()

# Cria um objeto de data representando o último dia do ano atual (31 de Dezembro)
fim_do_ano = date(data_atual.year, 12, 31)

# Calcula a diferença entre as datas e extrai apenas a quantidade de dias inteiros
dias_restantes = (fim_do_ano - data_atual).days

# Exibe o cabeçalho no console
print("--- Calculadora de Dias para o Fim do Ano ---")

# Exibe a data de hoje formatada no padrão brasileiro (Dia/Mês/Ano)
print(f"Data de hoje: {data_atual.strftime('%d/%m/%Y')}")

# Exibe a quantidade de dias que faltam para o término do ano
print(f"Faltam {dias_restantes} dias para o ano acabar!")