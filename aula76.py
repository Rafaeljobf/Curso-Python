# Manipulando chaves e valores em dicionários
pessoa = {}

chave = 'nome'
pessoa[chave] = 'Rafael Filho'

print(pessoa[chave])

pessoa['sobrenome'] = 'Filho'

print(pessoa)

# del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome') is None:    # verifica se o dict possui a chave
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])