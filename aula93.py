# Try, except, else e finally

try:
    a = 18
    b = 0
    print("Linha 1")
    c = a / b
    print("Linha 2")
except ZeroDivisionError as error:
    print("Dividiu por zero.")
    print("MSG:", error)
    print('Nome:', error.__class__.__name__)
except NameError:
    print("Variável não definida")
except (TypeError, IndexError):
    print("TypeError + IndexError")
except Exception:
    print("ERRO DESCONHECIDO")

print('Continuar')