# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Fernanda', 1, 2, 3, 'Rafael']
tupla = 'Python', 'é', 'legal'

a, b, *_, c = lista
print(a, b, c)

print(*lista)
print(*string)
print(*tupla)

