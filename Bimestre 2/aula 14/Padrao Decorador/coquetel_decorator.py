from coquetel import Coquetel


class CoquetelDecorator(Coquetel):


    def __init__(self, coquetel):


        self.coquetel = coquetel

    def get_nome(self):


        nome = "{0} + {1}".format(self.coquetel.get_nome(), self.nome)

        return nome

    def get_preco(self):


        return self.coquetel.get_preco() + self.preco
