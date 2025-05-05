# Operadores lógicos
# 'and' -> ambos os termos devem ser verdadeiros
#

entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Digite a senha: ')

senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrou')
else:
    print('Saiu')