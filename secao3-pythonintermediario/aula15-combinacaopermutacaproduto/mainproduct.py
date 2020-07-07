from itertools import combinations, product

pessoas = ['Luiz', 'Andre', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']

for grupo in product(pessoas, repeat=2):
    print(grupo)