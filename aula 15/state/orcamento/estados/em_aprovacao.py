from orcamento.estado import EstadoDoOrcamento
from orcamento.estados.aprovado import Aprovado
from orcamento.estados.reprovado import Reprovado


class EmAprovacao(EstadoDoOrcamento):


    def aplica_desconto_extra(self, orcamento):


        if not self.desconto_aplicado:
            orcamento.adiciona_desconto_extra(orcamento.total * 0.02)
            self.desconto_aplicado = True
        else:
            print("Desconto já foi aplicado.")

    def aprova(self, orcamento):


        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):


        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):


        print("Orçamentos em aprovação não podem ser finalizados.")
