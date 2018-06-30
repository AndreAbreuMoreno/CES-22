# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Andre Moreno
# 1 semestre 2018

#Aula 6
# Exercicio 1


class Shape:
    geometric_type = 'Generic Shape'

    def area(self):
        raise NotImplementedError

    def get_geometric_type(self):
        return self.get_geometric_type

class Plotter:
    def plot(self, ratio, topleft):
        print ('Plotting at {}, ratio {}.'.format(topleft, ratio))

class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'

class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side

class RegularPolygon2(Polygon):
    geometric_type = 'Regular Polygon whith double side'

    def __init__(self, side):
        self.side = side*2


class Hexagon(RegularPolygon):
    pass

class doubleHexagon(RegularPolygon, RegularPolygon2):
    pass


hexagon2 = doubleHexagon(2)

hexagon = Hexagon(2)


print(hexagon2.__class__.__mro__)

print(hexagon.__class__.__mro__)