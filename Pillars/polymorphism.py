

class Clase1:
    def calculate(self, arg1, arg2):
        print("=== Calcular ===")


class Clase2(Clase1):
    def calculate(self, arg1, arg2):
        super().calculate(arg1, arg2)
        print(arg1 + arg2)

class Clase3(Clase1):
    def calculate(self, arg1, arg2):
        super().calculate(arg1, arg2)
        print(arg1 - arg2)