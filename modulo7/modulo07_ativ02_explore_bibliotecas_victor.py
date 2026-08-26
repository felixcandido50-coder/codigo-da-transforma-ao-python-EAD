from datetime import date


data_atual = date.today()

fim_do_ano = date(data_atual.year, 12, 31)

dias_restantes = (fim_do_ano - data_atual).days

print("--- Calculadora de Dias para o Fim do Ano ---")
print(f"Data de hoje: {data_atual.strftime('%d/%m/%Y')}")
print(f"Faltam {dias_restantes} dias para o ano acabar!")