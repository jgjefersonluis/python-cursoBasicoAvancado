carrinho =[]
carrinho.append(('produto 1', 30.50))
carrinho.append(('produto 2', 20))
carrinho.append(('produto 2', 50))

#produto, preco = carrinho[0]
#print(produto, preco)

total = sum([float(y) for x, y in carrinho])
#print(carrinho)
print(total)






