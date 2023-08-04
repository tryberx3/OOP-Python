

class SupClase:
    def __init__(self, valor3):
        self.valor1 = 1
        self.valor2 = 2
        self.valor3 = valor3

    def display(self):
        print(self.valor1, self.valor2, self.valor3)

class SubClase(SupClase):
    def __init__(self, arg, name):
        super().__init__(valor3=arg)
        self.name = name

tst = SubClase(arg=8, name="tryber")
tst.display()
print(tst.name)