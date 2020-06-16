"""
* Criar variáveis para nome (str),idade(int)
* Altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano de atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""
nome = 'Jeferson'
idade = 49
altura = 1.75
peso = 103
ano_atual = 2020
nascimento = ano_atual - idade
imc = peso/altura ** 2

print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} kg e seu imc é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')