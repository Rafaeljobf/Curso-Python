# groupby - agrupando valores (itertools)
from itertools import groupby
alunos = [
    {'nome': 'Rafael', 'nota': 'A'},
    {'nome': 'Fernanda', 'nota': 'B'},
    {'nome': 'Gabriel', 'nota': 'A'},
    {'nome': 'Lucilene', 'nota': 'C'},
    {'nome': 'Maria', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Alice', 'nota': 'B'},
    {'nome': 'Agnes', 'nota': 'A'},
    {'nome': 'Neto', 'nota': 'C'},
]

alunos.sort(key=lambda alunos: alunos['nota'])
alunos_agrupados = groupby(alunos, key=lambda alunos: alunos['nota'])

for chave, valor in alunos_agrupados:
    print(f"Nota: {chave}")
    for aluno in valor:
        print(aluno['nome'])
    print()


