# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MyError(Exception):
    ...

class AnotherError(Exception):
    ...

def levantar():
    erro = MyError('a', 'b', 'c')
    raise erro

try:
    levantar()
except (MyError, ZeroDivisionError) as errinho:
    print(errinho.__class__.__name__)
    print(errinho.args)
    print()
    erro2 = AnotherError('Vou lançar de novo')
    raise erro2 from errinho
