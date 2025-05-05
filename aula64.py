"""
Indtrodução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do código
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções python retornam None (nada).
"""

# def Print(a, b, c):
#     print(a, b, c)

# Print(1, 2, 3)
# Print(4, 5, 6)
    
def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Rafael')
saudacao('Fernanda')
saudacao('Gabriel')
saudacao()



