from dados import produtos, pessoas, lista

nova_lista = filter(lambda p: p['preco'] > 50, produtos)

for produto in nova_lista:
    print(produto)
