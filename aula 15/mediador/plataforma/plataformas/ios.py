from plataforma.plataforma import Plataforma


class IOS(Plataforma):

    def __init__(self, mediator):


        super(IOS, self).__init__(mediator)

    def recebe_mensagem(self, mensagem):


        print("IOS recebeu:", mensagem)
