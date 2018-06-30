# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programacao Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Andre Moreno
# 1 semestre 2018


class Implementar:
    def action(self):
        pass

class ObjetoA(Implementar):
    def action(self):
        print("Objeto A implementado")


class ObjetoB(Implementar):
    def action(self):
        print("Objeto B implementado")

#
class Bridge:
    def __init__(self, implementacao):
        self._Implementar = implementacao

    def operation(self):
        self._Implementar.action()


if __name__ == "__main__":
    bridge = Bridge(ObjetoA())
    bridge.operation()

    bridge = Bridge(ObjetoB())
    bridge.operation()