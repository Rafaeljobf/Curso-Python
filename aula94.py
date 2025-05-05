# try, except, else e finally
try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError:
    print('DIVIDIU POR ZERO')
finally:
    print('FECHAR ARQUIVO')