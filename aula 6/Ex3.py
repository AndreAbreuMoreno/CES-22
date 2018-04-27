# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Andre Moreno
# 1 semestre 2018

#Aula 6
# Exercicio 3

def list_all_guests(*args):
    if args is not None:
        for name in sorted(args):
            print(name)
    else: print("Nao ha convidados")

def list_names(**kwargs):
    if kwargs is not None:
        for name, surname in kwargs.items():
            print(name+" "+surname+" is one of the guests")
    else: print("Think about some guests ;)")

print("\nHere is a party prototype")
print("I want to invite:")
list_names(Lee = "Miller", Anna = "Bolena", Audrey = "Hepburn", Miss = "Moneypenny")
print("\nThat means:")
list_all_guests("Miller", "Bolena", "Hepburn", "Moneypenny")
