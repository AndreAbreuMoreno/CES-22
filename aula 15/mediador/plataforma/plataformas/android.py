from plataforma.plataforma import Plataforma


class Android(Plataforma):

    def __init__(self, mediator):


        super(Android, self).__init__(mediator)

    def recebe_mensagem(self, mensagem):


        print("Android recebeu:", mensagem)
