# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Andre Moreno
# 1 semestre 2018

#Aula 7
# Exercicio 1
import time
import threading

class Box(object):
    lock = threading.RLock()

    def __init__(self):
        self.total_items = 0

    def execute(self, n):
        Box.lock.acquire()
        self.total_items += n
        Box.lock.release()

    def add(self):
        Box.lock.acquire()
        self.execute(1)
        Box.lock.release()

    def remove(self):
        Box.lock.acquire()
        self.execute(-1)
        Box.lock.release()

def adder(name, box, items):
    while items > 0:
        print('Producer notify: item N %d added by %s'% (items, name))
        box.add()
        time.sleep(5)
        items -= 1

def remover(name, box, items):
    while items > 0:
        print('Consumer notify: item N %d popped by %s'% (items, name))
        box.remove()
        time.sleep(5)
        items -= 1

if __name__ == '__main__':
    items = 5
    print ("Producer notify: Adding items")
    box = Box()
    t1 = threading.Thread(target=adder, args=('Thread-1', box, items))
    t2 = threading.Thread(target=remover, args=('Thread-2', box, items))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("{} items still remain in the box".format(box.total_items))
