# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Rafael',
    'sobrenome': 'Filho',
    # 'idade': 900,
}

# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))

# print(list(pessoa.items()))

for chave, valor in pessoa.items():
    print(f'{chave.title()}: {valor}')