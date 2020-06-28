"""
1 - crie uma função1 que recebe uma funcao2 com parametro
e retorne o valor da funcao2 executada.

"""

def ola_mundo():
    return 'Ola mundo!'

def mestre(funcao):
    return funcao()

print(ola_mundo())


"""
2 - crie uma funçao1 que recebe uma funcao2 como parametro 
e retorne o valor da funcao2 executada. Faça a funcao1 executar duas
funções que recebam um número diferente de argumentos.
"""

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao}{nome}'

executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, 'Luis', saudacao='Bom dia!')
print(executando)
print(executando2)

