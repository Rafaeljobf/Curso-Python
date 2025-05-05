numero = input('Digite o número que você quer manipular: ')

print('O que deseja fazer com esse numero:')
decisao = input('[D]uplicar, [T]riplicar, [Q]uadruplicar. ')

def manipulacao(num, multiplicador):
    if multiplicador == 'D' or multiplicador == 'd':
        return int(num) * 2
    elif multiplicador == 't' or multiplicador == 'T':
        return int(num) * 3
    elif multiplicador == 'q' or multiplicador == 'Q':
        return int(num) * 4
    else:
        return print('Você não obedeceu as regras.')
    

print(manipulacao(numero, decisao))