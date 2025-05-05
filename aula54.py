"""
Excercício
Exiba os índices da lista
"""

lista = ['Rafael', 'Fernanda', 'Gabriel', 'Fofonilsons', 22]
indice = 0

while True:
    for item in lista:
        print(indice, item)
        indice += 1
    
    if indice == len(lista):
        break
    