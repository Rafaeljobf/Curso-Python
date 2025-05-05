# Dictionary comprehension e Set comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

dc = {
    chave.title(): valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

# dc = {
#     chave: valor
#     for chave, valor in lista
# }

# print(dict(lista))

s1 = {i ** 2 for i in range(10)}

print(sorted(s1))