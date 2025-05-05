def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args) 

print(
    executa(saudacao, 'Bom dia', 'Rafael')
    )

print(
    executa(saudacao, 'Boa tarde', 'Fernanda')
    )

