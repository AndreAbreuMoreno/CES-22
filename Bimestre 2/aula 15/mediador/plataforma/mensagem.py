from plataforma.mediator import Mediator
from plataforma.plataformas.ios import IOS
from plataforma.plataformas.android import Android


class MensagemMediator(Mediator):


    def __init__(self):

        self.contatos = []

    def adiciona(self, plataforma):

        self.contatos.append(plataforma)

    def envia(self, mensagem, plataforma):

        for contato in self.contatos:
            if (contato != plataforma):
                self.__definir_protocolo(contato)
                contato.recebe_mensagem(mensagem)

    def __definir_protocolo(self, contato):


        if (type(contato) == type(IOS)):
            print("Protocolo IOS")
        elif (type(contato) == type(Android)):
            print("Protocolo Android")
