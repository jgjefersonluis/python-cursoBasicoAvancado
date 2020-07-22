"""Descrição rápida e simples.
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nam finibus est ac massa congue imperdiet.

Nam egestas lectus gravida, commodo augue id, ultrices nisl.
Etiam a velit ultricies, vulputate est eget, ultricies ante.
Interdum et malesuada fames ac ante ipsum primis in faucibus.

"""


variavel_1 = 'valor 1'


def funcao(x, y):
    """Soma x e y

    :param x: Numero 1
    :type x: int or float
    :param y: Numero 2
    :type y: int or float

    :return: A soma entre x e y
    :type: int or float
    """
    return x + y


def multiplica(x, y, z=None):
    """Multiplica x, y, z

    Multiplica x, y e z. O programador por omitir a variavel
    z caso não tenha necessidade de usá-la.

    :param x: Numero 1
    :type x: int or float
    :param y: Numero 2
    :type y: int or float
    :param z: Numero 3
    :type z: int or float

    :return: A soma entre x, y e z
    :type: int or float

    """
    if z:
        return x * y
    else:
        return  x * y * z

variavel_2 = 'valor 2'
variavel_3 = 'valor 3'
variavel_4 = 'valor 4'

