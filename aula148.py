# Notas das exceptions em Python (add_notes, __notes__)
# https://docs.python.org/3/library/exceptions.html
# Adicionando notas em exceções (3.11.0)

class MyError(Exception):
    ...

class AnotherError(Exception):
    ...

def levantar():
    erro = MyError('a', 'b', 'c')
    erro.add_note('nota adicionada')
    raise erro

try:
    levantar()
except (MyError, ZeroDivisionError) as errinho:
    print(errinho.__class__.__name__)
    print(errinho.args)
    print()
    erro2 = AnotherError('Vou lançar de novo')
    erro2.add_note('segunda notinha')
    erro2.__notes__ += errinho.__notes__.copy()
    raise erro2 from errinho