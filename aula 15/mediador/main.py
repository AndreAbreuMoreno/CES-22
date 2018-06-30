from plataforma import MensagemMediator
from plataforma.plataformas import IOS, Android


def main():


    mediator = MensagemMediator()

    android = Android(mediator)
    ios = IOS(mediator)

    mediator.adiciona(android)
    mediator.adiciona(ios)

    android.envia_mensagem("Oi, eu sou o android")
    ios.envia_mensagem("Olá android, eu sou o IOS")


if __name__ == '__main__':
    main()
