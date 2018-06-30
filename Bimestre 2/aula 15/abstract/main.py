
import random


class PetShop:


    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print ("Olhe um", pet)
        print ("Ele ", pet.speak())
        print ("Ele come", self.pet_factory.get_food())

# Stuff that our factory makes


class Dog:
    def speak(self):
        return "late"

    def __str__(self):
        return "cachorro"


class Cat:
    def speak(self):
        return "mia"

    def __str__(self):
        return "gato"



class DogFactory:
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "comida de cachorro"


class CatFactory:
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "comida de gato"



def get_factory():

    return random.choice([DogFactory, CatFactory])()


shop = PetShop()
for i in range(3):
    shop.pet_factory = get_factory()
    shop.show_pet()
    print ("=" * 10)