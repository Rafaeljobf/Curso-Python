from datetime import datetime
from pytz import timezone


agora = datetime.now(timezone('Asia/Tokyo'))
print(agora)

sec_timestamp = agora.timestamp()
print(datetime.fromtimestamp(sec_timestamp, tz=timezone('Asia/Tokyo')))

print(sec_timestamp) # essa representação fica em base de dados.

# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz