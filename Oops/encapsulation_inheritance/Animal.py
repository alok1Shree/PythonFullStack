class Animal:
    def __init__(self, name, sound):
        self.__name = name
        self.__sound = sound

    #Getter Method
    def get_Name(self):
        return self.__name

    #Getter Method
    def get_Sound(self):
        return self.__sound

    #Methods inhertted by ALl child classes
    def make_sound(self):
        print(f"{self.__name} says {self.__sound}")

    def sleep(self):
        print(f"{self.__name} is sleeping...")