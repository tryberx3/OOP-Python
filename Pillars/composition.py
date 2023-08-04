

class Motor:
    def encender(self):
        print("Motor encendido")

    def apagar(self):
        print("Motor apagado")

class Automovil:
    def __init__(self):
        self.motor = Motor()  # Composición

    def encender_auto(self):
        self.motor.encender()

    def apagar_auto(self):
        self.motor.apagar()

auto = Automovil()
auto.encender_auto()  # Salida: "Motor encendido"
auto.apagar_auto()  # Salida: "Motor apagado"
