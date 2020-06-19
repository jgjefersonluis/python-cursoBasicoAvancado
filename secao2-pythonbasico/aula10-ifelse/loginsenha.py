usuario = input('Nome de Usuário: ')
senha = input('Senha do Usuário: ')

usuario_bd = 'jeferson'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
     print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos.')

