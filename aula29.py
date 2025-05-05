"""
try / except
try -> tentar executar o código
except -> ocorreu um erro ao tentar executar
"""

numero_str = input('Vou dobrar o numero que vc digitar: ')

try:
    numero_float = float(numero_str)
    print(f'FLOAT: {numero_float}')
    print(f'o dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um número')

