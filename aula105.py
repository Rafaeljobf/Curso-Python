# Decoradores com parâmetros
def decorator(func):
    print("Decoradora 1")

    def inner(*args, **kwargs):
        print("Aninhada")
        result = func(*args, **kwargs)
        return result + 20
    return inner


@decorator
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)