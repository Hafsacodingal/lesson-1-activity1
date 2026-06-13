from abc import ABC, abstractmethod

class Instrument(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

class Guitar(Instrument):
    def __init__(self, name):
        super().__init__(name)
    
    def sound(self):
        print(self.name, "goes: Twang Twang")

class Drum(Instrument):
    def __init__(self, name):
        super().__init__(name)
    
    def sound(self):
        print(self.name, "goes: Boom")

g1 = Guitar("Guitar")
d1 = Drum("Drum")

g1.sound()
d1.sound()