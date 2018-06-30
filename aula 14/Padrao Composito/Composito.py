
class componente:
    def getChild(self, index):
        pass

    def add(self, componente):
        pass

    def remove(self, index):
        pass

    def operation(self):
        pass



class composito(componente):
    def __init__(self):
        componente.__init__(self)
        self._children = []

    def getChild(self, index):
        return self._children[index]

    def add(self, componente):
        self._children.append(componente)

    def remove(self, index):
        self._children.remove(index)

    def operation(self):
        for i in range(len(self._children)):
            self._children[i].operation()



class Vertice(componente):
    def __init__(self, index):
        componente.__init__(self)
        self._idx = index

    def operation(self):
        print("Vertice " + str(self._idx))


if __name__ == "__main__":
    composito = composito()

    for i in range(5):
        composito.add(Vertice(i))

    composito.operation()