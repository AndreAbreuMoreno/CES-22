from orcamento.estado import EstadoDoOrcamento
from orcamento.estados.finalizado import Finalizado


class Aprovado(EstadoDoOrcamento):


    def aplica_desconto_extra(self, orcamento):

        if not self.desconto_aplicado:
            orcamento.adiciona_desconto_extra(orcamento.total * 0.05)
            self.desconto_aplicado = True
        else:
            print("Desconto já foi aplicado.")

    def aprova(self, orcamento):


        print("O orçamento já está aprovado.")

    def reprova(self, orcamento):


        print("O orçamento já está aprovado, não pode ser reprovado.")

    def finaliza(self, orcamento):


        orcamento.estado_atual = Finalizado()
