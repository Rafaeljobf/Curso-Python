

lista = ['Rafael', 'Fernanda', 'Gabriel']
lista.append('Fofs')


for indice, nome in enumerate(lista):
    print(indice, nome)

for item in enumerate(lista):    
    indice, nome = item
    print(indice, nome)

for tupla_enumerada in enumerate(lista):
    for valor in tupla_enumerada:
        print(valor)