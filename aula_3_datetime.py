# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'

data_inicio = datetime.strptime('16/04/2005 18:00:00', fmt)
data_fim = datetime.strptime('22/02/2006 18:00:00', fmt)
delta = timedelta(days=10)

print(data_inicio + delta)
print(data_inicio - delta)
print(data_fim + relativedelta(seconds=33))

delta2 = relativedelta(data_fim, data_inicio)
print(delta2, delta2.months, delta2.days)



# print(data_inicio > data_fim)
# delta = data_fim - data_inicio
# print(delta, delta.total_seconds())