import os
import json

def to_do_list(comando):
    match comando:
        case 'listar':
            ...
        case 'desfazer':
            if len(lista_atual) == 0:
                print('Nenhuma tarefa para desfazer')
                return
            else:
                tarefa = lista_atual.pop()
                tarefas_refazer.append(tarefa)
        case 'refazer':
            if len(tarefas_refazer) == 0:
                print('')
                print("NÃO HÁ TAREFAS PARA REFAZER")
            else:
                lista_atual.append(tarefas_refazer[-1])
                tarefas_refazer.pop(-1)
        case 'limpar tela':
            os.system('cls')
        case _:
            lista_atual.append(comando)

with open('aula119.json', 'r') as arquivo_salvo:
    lista_atual = json.load(arquivo_salvo)

tarefas_refazer = []
  
while True:
    print('Comandos: listar, desfazer, refazer, limpar tela')
    resposta = input('Digite uma tarefa ou comando: ')
    to_do_list(resposta)
    
    print('')
    if len(lista_atual) == 0:
        print('NÃO HÁ TAREFAS')
        print('')
        continue
    else:
        print('TAREFAS:')
        for tarefa in lista_atual:
            print(tarefa)
        print('')
    
    with open('aula119.json', 'w') as arquivo:
        json.dump(lista_atual, arquivo, ensure_ascii=False, indent=2)
