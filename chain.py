

# Return Chain

class Chain:
    def method1(self):
        print("Hola")
        return self

    def method2(self):
        print("Mundo")
        return self
    
obj = Chain().method1().method2()