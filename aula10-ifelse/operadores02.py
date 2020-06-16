nome = input('Qual é o seu nome?')
idade = input('Qual é a sua idade?')

idade = int(idade)

# Limite para pegar empréstimo
idade_menor = 20 #muito jovem
idade_maior = 30 #passou da idade

if idade > idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o emprestimo.')
else:
    print(f'{nome} NÃo pode pegar o empréstimo.')
