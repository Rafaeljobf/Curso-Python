from aula128_a import CAMINHO_ARQUIVO, Pessoa
import json

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)

    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3 = Pessoa(**dados[2])
    
    print(vars(p1))
    