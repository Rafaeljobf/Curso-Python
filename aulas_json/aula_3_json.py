# json.dump e json.load com arquivos
import json
import os

NOME_ARQUIVO = 'aula_3_json.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

filme = {
    'title': 'O Senhor Dos Anéis: A Sociedade Do Anel',
    'original_title': 'The Lord of The Rings: the Fellowship of The Ring', 
    'is_movie': True, 'imdb_rating': 8.8, 'year': 2001, 
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=3)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    filme_do_json = json.load(arquivo)
    print(filme_do_json)