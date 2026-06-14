class Pet:
    def __init__(self, name):
        self.name = name
        self.__health = 100

    def make_sound(self):
        print(self.name, "makes a sound")

    def get_health(self):
        return self.__health

    def set_health(self, value):
        if value >= 0 and value <= 100:
            self.__health = value

class Dog(Pet):
    def make_sound(self):
        print(self.name, "says Woof!")

class Cat(Pet):
    def make_sound(self):
        print(self.name, "says Meow!")

pets = [Dog("Tommy"), Cat("Kitty")]

for pet in pets:
    pet.make_sound()
    pet.set_health(80)
    print(pet.name, "health:", pet.get_health())
    print()