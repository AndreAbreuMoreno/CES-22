from orcamento.estado import EstadoDoOrcamento
from orcamento.estados.finalizado import Finalizado


class Reprovado(EstadoDoOrcamento):


    def aplica_desconto_extra(self, orcamento):

        print("Orçamentos reprovados não recebem desconto extra.")

    def aprova(self, orcamento):


        print("Orçamento já está reprovado, não pode ser aprovado.")

    def reprova(self, orcamento):

        print("O orçamento já está reprovado, não pode ser reprovado novamente.")

    def finaliza(self, orcamento):

        orcamento.estado_atual = Finalizado()
