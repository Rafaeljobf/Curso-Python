# + concatena listas

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)

if lista_a == lista_c:
    print('Listas iguais')