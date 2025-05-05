# Empacotamento e desempacotamento em dicionários

pessoa = {
    'nome': 'Rafael',
    'sobrenome': 'Filho',
}

dados_pessoa = {
    'idade': 20,
    'altura': 1.73
}

pessoas_completa = {**pessoa, **dados_pessoa}

def mostro_argumentos_nomeados(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave.title()}: {valor}')

mostro_argumentos_nomeados(**pessoas_completa)