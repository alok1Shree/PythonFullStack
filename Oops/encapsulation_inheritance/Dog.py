from .Animal import Animal


class Dog(Animal):
    def __init__(self, name, bread):
        super().__init__(name, "Woof!")
        self.__bread = bread

    def eat(self):
        print("You eaten the dog")

    def get_bread(self):
        return self.__bread

