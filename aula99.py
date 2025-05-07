# from sys import path

# # import aula99_package
# from aula99_package.modulo import soma_do_modulo
# from aula99_package import modulo
# from aula99_package.modulo import *


# print(soma_do_modulo(1, 2)) # importaçao mais especifica, codigo mais limpo
# print(modulo.soma_do_modulo(1, 2))
# print(soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel) # erro: nao está incluso no __all__ do módulo

from aula99_package.modulo import fala_oi, soma_do_modulo

fala_oi()
print(soma_do_modulo(1, 2))