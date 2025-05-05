"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar  Ler  Alterar Apagar = lista[i] (CRUD)
"""
lista = [1, 2, 3, 4, 5]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append('BBB')
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista,f'removidos: {ultimo_valor}')