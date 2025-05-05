numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('O número inteiro é par')
    else:
        print('O número inteiro ímpar')
except:
    print('Não é um número inteiro')

