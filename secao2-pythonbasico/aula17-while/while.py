"""
while em python - aula 07
utilizado para realizar ações enquanto
uma condição for verdadeira

Requisitos: Entender condições e operadores
"""
x = 0 # coluna
while x < 10:
    y = 0 # linha

    while y < 5:
      #  print(f'X vale {x} e Y vale {y}')
        print(f'({x},{y})')
        y += 1

    x += 1 # x = x + 1

print('Acabou!')






'''
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break

    print(x)
    x = x + 1

print('Acabou')
'''

'''
x = 0
while x < 100:
    print(x)
    x = x + 1
print('Acabou')
'''

'''
while True: # loop infinito
    nome = input("Qual o seu nome? ")
    print(f'Ola, {nome}!')

print('Não será executada.')
'''