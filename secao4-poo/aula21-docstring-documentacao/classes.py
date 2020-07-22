"""Descrição rápida e simples.
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nam finibus est ac massa congue imperdiet.

Nam egestas lectus gravida, commodo augue id, ultrices nisl.
Etiam a velit ultricies, vulputate est eget, ultricies ante.
Interdum et malesuada fames ac ante ipsum primis in faucibus.

"""

class MinhaClasse:
    """Documentação normal

    Conforme qualquer outra documentação que você tenha
    usado anteriormente.
    """
    atributo = 1
    atributo2 = 'Valor'

    def __init__(self, texto):
        """Inicializa os dados

        :param texto: o texto da classe
        :type texto: str
        """
        self.texto = texto
        self.exibe_texto(texto)

    @staticmethod
    def exibe_texto(texto):
        """Método que exibe um texto de 100 caracteres
        na tela

        :param texto: Um texto de 100 caracteres na tela
        :type: str

        :raises ValueError: Se o texto tiver mais que 100 caracteres
        :raises TypeError: Se o texto não for uma strig
        """
        if not isinstance(texto, str):
            raise TypeError('Texto precisa ser uma string.')

        if len(texto) > 100:
            raise ValueError('Texto precisa ter 100 caracteres ou menos')
        return texto

