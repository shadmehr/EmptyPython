""" This is an example of factory method in Python"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """Represent an animal object.

    Args:
        ABC (object): the absract base class.
    """

    def __init__(self, pet_name):
        self.name = pet_name
        self.food = "any"
        super().__init__()

    @abstractmethod
    def speek(self):
        """Returns the sound that animal makes
        """
        pass

    def setfood(self, value):
        self.food = value

    def getfood(self):
        return self.food

    def __str__(self):
        return "Animal"


class Cat(Animal):
    def speek(self):
        """Returns the sound that animal makes
        """
        return "Meow"

    def __str__(self):
        return "Cat:" + self.name


class Dog(Animal):
    def speek(self):
        """Returns the sound that animal makes
        """
        return "Woof"

    def __str__(self):
        return "Dog:" + self.name


def get_pet(pet_name="dog"):

    if pet_name == "cat":
        return Cat(pet_name)

    return Dog(pet_name)


def main():
    print(get_pet())

    dog = get_pet("dog")
    cat = get_pet("cat")

    print(dog.speek())
    print(cat.speek())
    print(dog.food)


if __name__ == "__main__":
    main()
