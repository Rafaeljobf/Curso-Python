# Calculadora com while

while True:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    operador = input('Digite o operador lógico (+, -, * ou /): ')


    numeros_validos = None

    try:
        num1 = float(num1)
        num2 = float(num2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números não são válidos.')
        continue

    operadores_permitidos = '+-/*' 

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Você digitou mais de um operador.')
        continue

    if operador == '+':
        soma = num1 + num2
        print(soma)
    elif operador == '-':
        subtracao = num1 - num2
        print(subtracao)
    elif operador == '*':
        multiplicacao = num1 * num2
        print(multiplicacao)
    elif operador == '/':
        divisao = num1 / num2
        print(divisao)
    else:
        print('Nunca deveria chegar aqui')

    sair = input('Você deseja sair? [s]im ').lower().startswith('s')

    if sair:
        break