"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Rafael', 'Fernanda']
lista_b = lista_a.copy()

lista_a[0] = 'Fofilho'
print(lista_a)
print(lista_b)