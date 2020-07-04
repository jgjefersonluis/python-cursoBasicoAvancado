"""
Zip - Unindo iteraveis
Zip_longest - Itertools
"""
from itertools import zip_longest
### Código
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']

# Código
estados = ['SP', 'MG', 'BA']

#cidades_estados = zip(estados, cidades)

cidades_estados = zip_longest(estados, cidades, fillvalue='Estado')

print(list(cidades_estados))


"""
for valor in cidades_estados:
    print(valor)

"""