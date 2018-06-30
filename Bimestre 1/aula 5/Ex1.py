# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Andre Moreno
# 1 semestre 2018

#Aula 5
# Exercicio 1


import abc


class Cafe(object):
    def __init__(self, cafe, preco):
        self.cafe = cafe
        self.preco = preco

    def get_cafe(self):
        return "Escolheu {}".format(self.cafe)

    @staticmethod
    def get_cobertura(sabor):
        return "O saber e {}".format(str(sabor))

    @classmethod
    def dobro_cobertura(cls):
        return "Dobro de {}".format(cls.sabor)

    @abc.abstractmethod
    def pao_na_chapa():
        pass


class PaoNaChapa(Cafe):
    def __init__(self, time):
        self.time = time

    def pao_na_chapa(self):
        return "Tempo estimado de  {} min".format(self.time)

cafe_expresso = Cafe("cafe expresso", 1.80)
cafe_expresso.get_cobertura("chatilly")
print("Voce escolheu {0}, preco {1} ".format(cafe_expresso.cafe, cafe_expresso.preco))
