

from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def __init__(self, atribute1, atribute2):
        self.atribute1 = atribute1
        self.atribute2 = atribute2

class Concrete(Interface):
    def __init__(self, atribute3):
        super().__init__(atribute1=10, atribute2=20)
        self.atribute3 = atribute3

tst = Concrete(atribute3=30)