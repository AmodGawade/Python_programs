#!/Users/amod/venv/bin/python
# name : Amod
# date : 1 april 2020
import argparse


# Function definition
def print_me():
    print("Test print")


def add(a, b):
    print(a+b)


def sub(x, y):
    '''doc string
    this method is subtraction
    it takes argument x, y
    '''
    c = x - y
    print(c)


def multiply(a, b):
    print(int(a)*int(b))


def divide(a, b):
    print(int(a)/int(b))




# main Program
#a = input("Enter an integer value : ")
#b = input("Enter an integer value : ")
#op = input("Enter either * or / or + or -")

parser = argparse.ArgumentParser(description="Math Calculation")
parser.add_argument('a', type=int, help="Enter only integers")
parser.add_argument('b', type=int, help="Enter only integers")
parser.add_argument('op', type=str, help="Enter only symbols * or / or + or --")
args = parser.parse_args()
# print(args)
a = args.a
b = args.b
op = args.op


if op == "*":
    multiply(a, b)
elif op == "/":
    divide(a, b)
elif op == "+":
    add(a, b)
elif op == "-":
    sub(int(a), b)
else:
    print("Incorrect input")
