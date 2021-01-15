""" This is an example of singleton in Python"""

import threading
import factory_method as fm
from abc import ABC


class PetCache(ABC):
    """Represents the cache for pets
    """
    current_instance = None
    lock = threading.Lock()

    def __init__(self):
        self.items = dict()
        super().__init__()

    def AddPet(self, pet):
        self.items[pet] = pet

    @staticmethod
    def Current():
        if PetCache.current_instance is not None:
            return PetCache.current_instance

        # lock all thread before creating the object.
        PetCache.lock.acquire()
        try:
            # double check lock pattern
            if PetCache.current_instance is None:
                PetCache.current_instance = PetCache()
        finally:
            PetCache.lock.release()

        return PetCache.current_instance

    def Show(self):
        for i in self.items:
            print(i)


def main():
    c1 = PetCache.Current()
    c2 = PetCache.Current()

    c1.AddPet(fm.Cat("cat1"))
    c2.AddPet(fm.Dog("dog1"))

    c1.Show()
    c2.Show()
    pass


if __name__ == "__main__":
    main()
