while True:
    print()
    num_1 = input('Digite um numero: ')
    num_2 = input('Digite outro numero')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um numero.2')
        continue

        num_1 = int(num_1)
        num_2 = int(num_2)

        # + - / *
        if operador == '+':
            print(num_1 + num_2)
        elif operador == '-':
            print(num_1 - num_2)
        elif operador == '/':
            print(num_1 / num_2)
        elif operador == '*':
            print(num_1 * num_2)
        else:
            print('Operador inválido!')