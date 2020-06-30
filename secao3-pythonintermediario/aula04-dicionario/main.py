import copy

d1= {1: 'a', 2: 'b', 3: 'c', 'd' : ['Luiz', 'Otavio']}
# v = d1.copy()
v=copy.deepcopy(d1)

v[1] = 'Luiz'
v['d'][0] = 'Dante'

# print(v['d'][0])

print(d1)
print(v)
