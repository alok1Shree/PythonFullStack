"""from .Dog import Dog
from .Cat import Cat

dog = Dog("Bruno", "Labrador")
cat = Cat("Whiskers", True)

dog.make_sound()
dog.eat() #Specific method created in the Dog class
dog.sleep()


cat.make_sound()
cat.purr()

print(dog.get_Sound())
print(cat.get_Sound())
print(dog.sleep())
print(cat.purr())
print(dog.get_bread())"""

# PARENT CLASS
class Animal:

    def __init__(self, name, sound):
        self.__name  = name    # private
        self.__sound = sound

    # Getters
    def get_name(self):  return self.__name
    def get_sound(self): return self.__sound

    # Methods inherited by ALL children
    def make_sound(self):
        print(f"{self.__name} says: {self.__sound}")

    def sleep(self):
        print(f"{self.__name} is sleeping... 💤")


# CHILD CLASS — inherits from Animal using (Animal)
class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name, "Woof")   # calls Animal's __init__
        self.__breed = breed             # NEW field only Dog has

    def get_breed(self): return self.__breed

    # NEW method — only Dog has this
    def fetch(self):
        print(f"{self.get_name()} fetches the ball! 🎾")


# ANOTHER CHILD
class Cat(Animal):

    def __init__(self, name, is_indoor):
        super().__init__(name, "Meow")
        self.__is_indoor = is_indoor

    def purr(self):
        print(f"{self.get_name()} purrs... 😻")


# USING THEM
d = Dog("Bruno", "Labrador")
c = Cat("Whiskers", True)

d.make_sound()   # Inherited → "Bruno says: Woof"
d.sleep()        # Inherited → "Bruno is sleeping..."
d.fetch()        # Dog's own

c.make_sound()   # Inherited → "Whiskers says: Meow"
c.purr()         # Cat's own

print(d.get_breed())   # Labrador