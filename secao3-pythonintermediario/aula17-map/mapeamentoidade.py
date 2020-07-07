from dados import produtos, pessoas, lista

def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p

nomes = map(aumenta_idade, pessoas)

for pessoas in nomes:
    print(pessoas)