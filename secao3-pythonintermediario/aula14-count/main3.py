from itertools import count

contador = count()
lista = ['Luis', 'João', 'Maria', 'José', 'Silva', 'Eduardo']

lista = zip(contador, lista)
print(list(lista))

