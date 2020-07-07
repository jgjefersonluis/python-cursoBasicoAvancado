from itertools import combinations, permutations

pessoas = ['Luiz', 'Andre', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']

for grupo in permutations(pessoas, 2):
    print(grupo)