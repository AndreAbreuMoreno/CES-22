# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programacao Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Andre Moreno
# 1 semestre 2018

from bebidas import Cachaca
from adicionais import Acuca, Suco


def main():


    coquetel = Cachaca()
    print(coquetel.get_nome(), "= R$", str(coquetel.get_preco()))

    coquetel = Suco(coquetel)
    print(coquetel.get_nome(), "= R$", str(coquetel.get_preco()))

    coquetel = Acuca(coquetel)
    print(coquetel.get_nome(), "= R$", str(coquetel.get_preco()))


if __name__ == '__main__':
    main()
