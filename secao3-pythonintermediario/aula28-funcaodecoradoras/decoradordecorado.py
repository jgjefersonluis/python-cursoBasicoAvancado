
def master(funcao):
    def slave():
        print('Agora estou decorada.')
        funcao()
    return slave


@master
def fala_oi():
    print('Oi')


fala_oi()
