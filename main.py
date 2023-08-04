

class Tsst:
    __private = {"password":"12345"}

    def __init__(self, elements):
        self.elements = elements

    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, index, value):
        self.elements[index] = value

    def __call__(self):
        print(self.elements)

numbers = Tsst(elements=[1,2,3,4,5])
print(numbers[1])
numbers[1] = 9
print(numbers[1])