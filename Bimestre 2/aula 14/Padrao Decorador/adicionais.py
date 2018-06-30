from coquetel_decorator import CoquetelDecorator


class Acuca(CoquetelDecorator):

    def __init__(self, coquetel):

        # Passa o coquetel para o contrutor do decorator
        super().__init__(coquetel)

        # Dados do adicional
        self.nome = "Açucar"
        self.preco = 0.50


class Limao(CoquetelDecorator):

    def __init__(self, coquetel):

        # Passa o coquetel para o contrutor do decorator
        super().__init__(coquetel)

        # Dados do adicional
        self.nome = "Limão"
        self.preco = 0.75

class Refrigerante(CoquetelDecorator):

    def __init__(self, coquetel):

        # Passa o coquetel para o contrutor do decorator
        super().__init__(coquetel)

        # Dados do adicional
        self.nome = "Refrigerante"
        self.preco = 1.0


class Suco(CoquetelDecorator):


    def __init__(self, coquetel):

        # Passa o coquetel para o contrutor do decorator
        super().__init__(coquetel)

        # Dados do adicional
        self.nome = "Suco"
        self.preco = 2.0