# Classes Decoradoras (Decorator Classes)

class Multiplicar:
    def __init__(self, multiplicador):
        self.multiplicador = multiplicador
    
    def __call__(self, func):
        def interno(*args):
            resultado = func(*args)
            return resultado * self.multiplicador
        return interno
    
@Multiplicar(10)
def soma(x, y):
    return x + y

dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)