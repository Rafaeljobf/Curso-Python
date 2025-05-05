# isintance - para saber se objeto é de determinado tipo
lista = [
    'a', 9, 3.14, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Rafael'},
]

for item in lista:
    if isinstance(item, set):
        item.add('foda')
        print(item)
    
    elif isinstance(item, (int, float)):
        print(item, item ** 2)
    
    else:
        print('OUTRO')
        print(item)