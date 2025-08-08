import os
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo

caminho_arquivo = 'aula116-2.txt'

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Linha 1')

os.remove(caminho_arquivo)