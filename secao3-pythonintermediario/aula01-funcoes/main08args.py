"""
Funções (def) em Python - *args **kwargs -
aula 16 (parte 3)
"""
def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6

var = func(1, 2, 3, 4, 5, nome='Luiz', a6='5')
print(var)