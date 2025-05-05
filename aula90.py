# dir, hasattr e getattr em Python
string = 'Rafael'
metodo = 'upper1'

if hasattr(string, metodo):
    print('existe upper')
    print(getattr(string, metodo)())
else:
    print(f'não existe o método {metodo}')