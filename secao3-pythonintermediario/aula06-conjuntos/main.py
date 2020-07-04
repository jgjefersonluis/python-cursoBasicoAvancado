# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos

s1 = {1,2,3,4,5}

for v in s1:
    print(v)
#####################
a1 = set()
a1.add(1)
a1.add(2)
a1.discard(2)

print(a1)
######################
e1 = set()
#e1.update('Python')
e1.update([1,2,3,4,5], {5,6,7,8})

print(e1)
#######################
l1 = {1,2,1,1,3,4,5,6,6,6,6,6,7,8,9, 'Luiz', 'Luis'}
l1 = set(l1)
l1 = list(l1)

print(l1(-1))
#############################



