from orcamento import Orcamento, Item


def main():


    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item 01', 100))
    orcamento.adiciona_item(Item('Item 02', 50))
    orcamento.adiciona_item(Item('Item 03', 400))

    print("Orcamento total - em aprovacao")
    print(orcamento.total)
    print("\nAplicou desconto")
    orcamento.aplica_desconto_extra()
    print(orcamento.total)
    orcamento.aprova()
    print("\nOrcamento aprovado \n\nAplicou novo desconto")
    orcamento.aplica_desconto_extra()
    print(orcamento.total)
    print("\nOrcamento finalizado")
    orcamento.finaliza()


if __name__ == '__main__':
    main()
