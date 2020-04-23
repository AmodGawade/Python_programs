import printcls


class Amod_math(printcls.calculator):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        printcls.calculator.addition(self.a, self.b)

    def sub(self):
        printcls.calculator.subtraction(self.a, self.b)


if __name__ == "__main__":

    obj = Amod_math(10, 20)
    obj.add()
    obj.sub()

    obj2 = Amod_math(100, 200)
    obj2.add()
