"""
For / Else em Python
"""
variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith('j'):
        continue
        print(valor)
   # else:
   # print('Não existe uma palavra que comece com J.')
