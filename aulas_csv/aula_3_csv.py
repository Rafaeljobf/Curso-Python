# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'aula_3_csv.csv'

lista_clientes = [
    {'Nome': 'Luiz Otavio', 'Endereco': 'Av 1, 22'},
    {'Nome': 'Joao Silva', 'Endereco': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereco': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w') as arquivo:
    colunas = lista_clientes[0].keys()
    escritor = csv.writer(arquivo)

    escritor.writerow(colunas)

    for cliente in lista_clientes:
        escritor.writerow(cliente.values())