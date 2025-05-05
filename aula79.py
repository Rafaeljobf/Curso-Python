p1 = {
    'nome': 'Rafael',
    'sobrenome': 'Filho'
}

# print(p1['nome'])
# print(p1.get('nome'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'novo valor',
#     'idade': 20,
# })

# p1.update(nome= 'novo valor', idade= 20)

# tupla = ('nome', 'novo valor'), ('idade', 20)
lista = ['nome', 'novo valor'], ['idade', 20]
p1.update(lista)
print(p1)