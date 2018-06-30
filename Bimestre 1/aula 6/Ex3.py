# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Andre Moreno
# 1 semestre 2018

#Aula 6
# Exercicio 3

def inventario(*args):
    if args is not None:
        for nome in sorted(args):
            print(nome)
    else: print("Nao ha itens no inventario")

def lista(**kwargs):
    if kwargs is not None:
        for item, categoria in kwargs.items():
            print(item+", "+categoria+", consta no inventario")
    else: print("Seu inventário esta vazio")

print("\nExemplo de controle de inventario")
print("Itens no inventario")
lista(microondas = "eletrodomestico", geladeira = "eletrodomestico", mesa = "moveis", armario = "Moveis")
print("\nTipo de itens no inventario:")
inventario("eletrodomestico", "moveis")
