# try, except, else e finally
try:
    print('ABRIR ARQUIVO')
    # 8/0
except ZeroDivisionError:
    print('DIVIDIU POR ZERO')
else:
    print("SEM ERROS")
finally:
    print('FECHAR ARQUIVO')