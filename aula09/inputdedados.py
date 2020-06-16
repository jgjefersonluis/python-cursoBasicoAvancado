"""
Entrada de dados - Aula 03
"""
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

ano_nascimento = 2020 - int(idade)

print()
print(f'{nome} tem {idade} anos.'
      f'{nome} nasceu em {ano_nascimento}.')
