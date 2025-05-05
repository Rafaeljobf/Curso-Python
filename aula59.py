"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = '      Olha só que       ,      coisa interessante             '
lista_frases_cruas = frase.split(',')

lista_frases_formatada = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases_formatada.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases_formatada)

frases_unidas = '-'.join(lista_frases_formatada)
print(frases_unidas)