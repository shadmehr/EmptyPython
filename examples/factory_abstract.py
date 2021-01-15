""" This is an example of abstract factory pattern in Python"""

from abc import ABC, abstractmethod
from factory_method import Dog, Cat


class AnimalFactory(ABC):
    @abstractmethod
    def get(self):
        pass


class DogFactory(AnimalFactory):
    def get(self):
        return Dog("Dog1")


class CatFactory(AnimalFactory):
    def get(self):
        return Cat("Cat1")


class PetShop:
    def __init__(self, pet_factory=None):
        self.pet_factory = pet_factory

    def show(self):
        animal = self.pet_factory.get()
        print(animal)


def main():
    shop = PetShop(CatFactory())
    shop.show()


if __name__ == "__main__":
    main()
