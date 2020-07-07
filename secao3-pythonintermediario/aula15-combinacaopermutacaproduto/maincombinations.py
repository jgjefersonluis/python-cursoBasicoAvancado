"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
permutação - Ordem importa
Ambos não repetem valores únicos
produto - Ordem importa e repete valores únicos

"""

from itertools import combinations

pessoas = ['Luiz', 'Andre', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']

for grupo in combinations(pessoas, 2):
    print(grupo)