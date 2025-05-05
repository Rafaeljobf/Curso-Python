"""
Iterando strings com while
"""

# objetivo: receber uma string do usuario e colocar algo entre as letras 

nome = 'Rafael'
novo_nome = ''
tamanho_nome = len(nome)
indice = 0

while indice < tamanho_nome:
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)



