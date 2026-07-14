from .Animal import Animal

class Cat(Animal):
    def __init__(self, name, is_indoor):
        super().__init__(name, "Meow!")
        self.__is_indoor = is_indoor

    def get_is_indoor(self):
        return self.__is_indoor

    def purr(self):
        print(f"{self.get_Name()} is purr...")