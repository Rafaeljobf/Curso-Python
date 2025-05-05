# List comprehension em Python
# List comprehension é uma forma rápida para criar listas a partir de iteráveis

# print(list(range(10)))


# lista = [numero*2 for numero in range(10)]
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

########################################

# lista = [n for n in range(10) if n < 5]

novos_produtos = [
    {**produto} for produto in produtos
    if produto['preco'] > 10
]

print(novos_produtos, sep='\n')