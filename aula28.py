nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if len(nome or idade) == 0:
    print('Desculpe, você deixou campos vazios')
else:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome têm espaços')
    else:
        print('Seu nome não tem espaços')
    print(f'Seu nome possui {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

