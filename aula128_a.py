# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = 'aula128.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Rafael', 20)
p2 = Pessoa('Fernanda', 19)
p3 = Pessoa('Gabriel', 12)
bd = [vars(p1), vars(p2), vars(p3)]

with open (CAMINHO_ARQUIVO, 'w') as dados:
    json.dump(bd, dados, ensure_ascii=False, indent=2)