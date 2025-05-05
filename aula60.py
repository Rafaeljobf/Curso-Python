"""
Listas de listas e seus índices
"""
salas = [

    ['Maria', 'Fernanda'],

    ['Rafael'],

    ['Gabriel', 'Rafael Filho', 'Lucilene']
]

# print(salas[0][1])
# print(salas[1][0])
# print(salas[2][2])
# print(salas[2][3][2])

for sala in salas:
    print(f'a sala é {sala}')
    for aluno in sala:
        print(aluno)