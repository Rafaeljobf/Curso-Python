# Operador Lógico 'or'.
# False "dominante"
# true, true, true, false = false

entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Digite a senha: ')

senha_permitida = '123456'
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrou')
else:
    print('Saiu')


senha = input('Senha: ') or 'Sem senha.'
print(senha)