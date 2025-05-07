# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
def nao_aceito_string(n, d):
    if isinstance(n, str) or isinstance(d, str):
        raise TypeError('Strings não são aceitas nessa função')
    return True
    
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero.')
    return True
    
def divide(n, d):
    nao_aceito_string(n, d)
    nao_aceito_zero(d)
    return n / d

print(divide(1, 2))