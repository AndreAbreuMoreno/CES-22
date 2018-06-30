from orcamento.estado import EstadoDoOrcamento


class Finalizado(EstadoDoOrcamento):


    def aplica_desconto_extra(self, orcamento):


        print("Orçamentos finalizados não recebem desconto extra.")

    def aprova(self, orcamento):


        print("Orçamento já finalizado.")

    def reprova(self, orcamento):

        print("Orçamento já finalizado.")

    def finaliza(self, orcamento):


        print("Orçamento já finalizado.")
