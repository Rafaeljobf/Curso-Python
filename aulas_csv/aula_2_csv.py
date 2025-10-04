# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'teste.csv'

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha['ï»¿Nome'], linha['Idade'], linha['EndereÃ§o'] )