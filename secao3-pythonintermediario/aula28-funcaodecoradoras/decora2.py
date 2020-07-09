def master():
    def slave():
        print('Oi!')
    return slave

variavel = master()
variavel()

