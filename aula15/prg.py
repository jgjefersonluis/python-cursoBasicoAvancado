"""
Formatando valores com modificadores - Aula 05
:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)F -  Quantidade de casas decimais (float)
: ((CARACTERE) (> ou < ou ^) (Quantidade/Tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))
num_3 = 1
print(f'{num_3:0>10}')

num_4 = 1150
print(f'{num_4:0>10}')

print(f'{num_4:0<10}')

print(f'{num_4:0^10}')

nome = 'Jeferson Luis'
print(nome.lower()) # tudo minusculo
print(nome.upper()) # tudo maiusculo
print(nome.title()) # Primeiras letras maiusculas

print((50-len(nome))/2)

print(f'{nome:#^50}')

# nome_formatado = '{:@50}'.format(nome)
# print(nome_formatado)
