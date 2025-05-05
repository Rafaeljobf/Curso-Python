# Exemplo de uso do tipo set
import os

letras = set()
while True:
    letra = input('Digite uma palavra: ')
    letras.add(letra.lower())

    print(letras)

    if 'fefe' in letras:
        os.system('cls')
        print('Você acertou a palavra secreta!')
        break
