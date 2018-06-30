from orcamento.estados.em_aprovacao import EmAprovacao


class Orcamento(object):

    def __init__(self):

        self.__itens = []
        self.estado_atual = EmAprovacao()
        self.__desconto_extra = 0

    @property
    def total(self):


        total = 0.0

        for item in self.__itens:
            total += item.valor

        return total - self.__desconto_extra

    def adiciona_item(self, item):


        self.__itens.append(item)

    def aprova(self):

        self.estado_atual.aprova(self)

    def reprova(self):

        self.estado_atual.reprova(self)

    def finaliza(self):

        self.estado_atual.finaliza(self)

    def aplica_desconto_extra(self):

        self.estado_atual.aplica_desconto_extra(self)

    def adiciona_desconto_extra(self, desconto):


        self.__desconto_extra += desconto
