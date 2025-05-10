# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def sum_of_list(lista1, lista2):
    smaller_list = min(len(lista1), len(lista2))

    return [lista1[i] + lista2[i] for i in range(smaller_list)]
    

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

# print(zipper(cidades, estados))

print(sum_of_list(l1, l2))










