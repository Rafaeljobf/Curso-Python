numero_escolhido = 468522

while True: 
    chute = input("Digite um número de 1 a 1000000: ")

    chute_int = int(chute)

    if chute_int < 1 or chute_int > 1000000:
        print('Escolha um número válido')
    elif chute_int < numero_escolhido:
        print('O número é maior do que você escolheu')   
    elif chute_int > numero_escolhido:
        print('O número é menor do que você escolheu')       
    else:
        print('VOCÊ ACERTOU!')
        break
    continue