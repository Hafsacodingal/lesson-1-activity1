from abc import ABC , abstractmethod
class Animal(ABC):
    def __init__(self,name,habitat):
        self.name=name
        self.habitat=habitat
    
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self,name,habitat,breed):
        super().__init__(name,habitat)
        self.breed=breed

    def speak(self):
       print(f"{self.name} ({self.breed}) says: Woof! Woof!")

class Cat(Animal):
    def __init__(self, name, habitat,habit):
        super().__init__(name, habitat)
        self.habit=habit

    def speak(self):
        print(f"{self.name} ({self.habit}) says: Meow! Meow!")

d=Dog("Bruno","Home","Labroder")
d=Cat("Kitty","Home","jumping")
d.speak()
