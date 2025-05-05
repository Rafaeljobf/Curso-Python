import os

indices_permitidos = 'i', 'a', 'l', 's'
lista_compras = []

while True:
    print('Selecione uma opção:')
    pergunta = input('[i]nserir [a]pagar [l]istar [s]air: ')

    if pergunta not in indices_permitidos: # Volta à pergunta em caso de indice inválido
        continue

    if pergunta == 'i':        # Acrescentar itens à lista
        os.system('cls')
        adicionar_lista = input('O que deseja adicionar: ')
        lista_compras.append(adicionar_lista)

    if pergunta == 'l':     # Listar
        os.system('cls')
        if len(lista_compras) == 0:
            print('Não há o que listar')
            continue
        for indice, item in enumerate(lista_compras):
            print(indice, item)
        


    if pergunta == 'a':       # Apagar itens da lista
        for indice, item in enumerate(lista_compras):
            print(indice, item)
        if len(lista_compras) == 0:
            print('Não há o que apagar.')
            continue
        apagar_item = input('Digite o índice do que deseja apagar: ')
        if apagar_item.isdigit() == False:
            print('Digite apenas o número do índice.')
            continue
        apagar_item_int = int(apagar_item)
        if apagar_item_int >= len(lista_compras):
            print('Índice inválido.')
        else:
            del lista_compras[apagar_item_int]
        

    if pergunta == 's':     # Sair do laço
        break

        

    
    



