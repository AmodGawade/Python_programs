#!/Users/amod/venv/bin/python
# name : Amod
from Programs.Module_1 import add, sub
import Programs.converter as cvt
# import Programs.Module_1 as mod1


def multiply(a, b):
    print(int(a)*int(b))


def divide(a, b):
    print(int(a)/int(b))


if __name__ == '__main__':
    multiply(10, 20)
    divide(30, 5)
    add(9, 8)
    sub(2, 1)
    # Programs.Module_1.add(9,0)
    cvt.energy(1000)
    cvt.speed(90)



