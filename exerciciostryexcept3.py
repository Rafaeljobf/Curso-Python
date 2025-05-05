nome = input('Digite o seu nome: ')
tamanho_nome = len(nome)

try:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    elif tamanho_nome > 6:
        print('Seu nome é grande')
except:
    print('Você não digitou um nome')