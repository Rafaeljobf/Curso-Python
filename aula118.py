# Problemas
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('fofilho')
adiciona_clientes('gabriel', cliente2)
adiciona_clientes('fernanda', cliente2)
print(cliente2)

cliente3 = adiciona_clientes('ferdenilda')
cliente3.append('fofilson')
print(cliente3)