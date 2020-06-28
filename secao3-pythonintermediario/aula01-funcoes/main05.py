def suadacao(msg='Ola,', nome='usuário!'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'

variavel = suadacao()

print(variavel)
