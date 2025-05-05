primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')
int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)

if int_primeiro_valor > int_segundo_valor:
    print(f'O primeiro valor: {primeiro_valor} é maior que o segundo valor: {segundo_valor}')
elif int_segundo_valor > int_primeiro_valor:
    print(f'O segundo valor: {segundo_valor} é maior que o primeiro valor: {primeiro_valor}')
else:
    print('Os valores são iguais')
