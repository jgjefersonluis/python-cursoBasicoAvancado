nome = 'Luis'
idade = 48 #int
altura = 1.80 #float
e_maior = idade > 18 #bool
peso = 103
imc = peso/altura ** 2

print(nome, 'tem', idade, 'de idade e seu imc é: ', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é, {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f} '.format(nome, idade, imc))
