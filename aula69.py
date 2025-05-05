"""
args - argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# soma1_2_3 = soma(1, 2, 3)
# print(soma1_2_3)

# soma4_5_6 = soma(4, 5, 6)
# print(soma4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(sum(numeros))



