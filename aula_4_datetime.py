# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

# data = datetime(2025, 4, 16, 7, 59, 23)
data = datetime.strptime('2025-04-16 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime('%d/%m/%Y'))
print(data.strftime('%H:%M:%S'))
print(data.strftime('%Y'))
