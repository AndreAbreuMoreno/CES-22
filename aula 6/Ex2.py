# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Andre Moreno
# 1 semestre 2018

#Aula 6
# Exercicio 2

import time
def timer_decorator(func):
    def wrapper():
        start = time.time()
        func()
        print('%s took %s seconds to run' % (func.__name__, time.time() - start))
    return wrapper

@timer_decorator
def sleeper():
    time.sleep(3)

