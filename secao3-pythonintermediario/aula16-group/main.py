from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Leticia', 'nota': 'B'},
    {'nome': 'Fabio', 'nota': 'A'},
    {'nome': 'Joana', 'nota': 'C'},
    {'nome': 'Ana', 'nota': 'D'},
    {'nome': 'Andre', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'B'},
    {'nome': 'Luisa', 'nota': 'A'},
    {'nome': 'Marcia', 'nota': 'C'},
    {'nome': 'Paulo', 'nota': 'B'},
]

ordena = lambda item: item ['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
   va1, va2 = tee(valores_agrupados)
   print(f'Agrupamento: {agrupamento}')

   for aluno in va1:
       print(f'\t{aluno}')

   quantidade = len(list(va2))
   print(f'{quantidade} alunos tiraram a nota {agrupamento}')
   print()


"""
alunos.sort(key=lambda item: item['nota'])
for aluno in alunos:
    print(aluno)
"""
