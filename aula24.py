# Operadores "in" e "not in"
# 0  1  2  3  4  5  6 
# F  O  F  I  L  H  O
#-7 -6 -5 -4 -3 -2 -1

# nome = 'Fofilho'
# print(nome[-3])
# print(nome[4])
# print('l' in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
