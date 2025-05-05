# Sistema de perguntas e respostas
import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '2', '4', '5'],
        'Resposta': '4',       
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['10', '20', '45', '25'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['10', '2', '4', '5'],
        'Resposta': '5',
    },
]
qtd_acertos = 0

for questao in perguntas:
    print(questao['Pergunta'])
    i = 0

    opcoes = questao['Opções']
    for opcao in opcoes:
        print(f'{i})', opcao)
        i += 1
    print()

    resposta_usuario = input('Escolha uma opção: ')
    
    acertou = False
    resposta_int = None
    qtd_opcoes = len(opcoes)

    if resposta_usuario.isdigit():
        resposta_int = int(resposta_usuario)
    
    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < qtd_opcoes:
            if opcoes[resposta_int] == questao['Resposta']:
                acertou = True

    

    if acertou:
        print('Acertou!')
        qtd_acertos += 1
    else:
        print('Errou!')
    print()

print(f'Você acertou {qtd_acertos} de', len(perguntas), 'perguntas!')

    
    
    
    