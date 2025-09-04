# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
total_parcelas = 60
valor_parcela = valor_total/total_parcelas

data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final_emprestimo = data_emprestimo + delta_anos

for parcela in range(total_parcelas):
    data_emprestimo_formatada = data_emprestimo.strftime("%d/%m/%Y")
    print(f'{data_emprestimo_formatada} R${valor_parcela:,.2f}')
    data_emprestimo += relativedelta(months=1)

print()
print(f'Você pegou R${valor_total:,.2f} para pagar em {delta_anos.years} anos. '
      f'Totalizando {total_parcelas} parcelas no valor de R${valor_parcela:,.2f}')
