# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu um erro', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()

with my_open('aula153.txt', 'w') as objeto:
    objeto.write('Linha 1\n')
    objeto.write('Linha 2\n', 123)
    objeto.write('Linha 3\n')
    print('WITH', objeto)