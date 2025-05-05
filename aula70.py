# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
    
print(multiplicar(1, 2, 3, 4, 5))

# Crie uma função que diz se um número é par ou ímpar
# Retorne se o número é par ou ímpar

def parouimpar(num):
    if num % 2 == 0:
        return f'{num} é PAR'
    return f'{num} é ÍMPAR'




while True:
    num = input('Digite um número: ')
    try:
        if num.isdigit:
            int_num = int(num)
            print(parouimpar(int_num))
    except ValueError:
        print('Você não digitou um número.')
        break

