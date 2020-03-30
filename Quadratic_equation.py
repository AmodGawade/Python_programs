#!/Users/amod/venv/bin/python
import cmath
# Author name : Amod
# Date : 20 march 2020

print("Program starts")

# Asking inputs from user

print("A quadratic equation is of the form ax2 + bx + c = 0")
a = input("Enter a value for a : ")
b = input("Enter a value for b : ")
c = input("Enter a value for c ; ")

# Solving the equation
D = int(b)**2 - 4*int(a)*int(c)
sol_1 = ((-int(b) - cmath.sqrt(D))/2*int(a))
sol_2 = ((-int(b) + cmath.sqrt(D))/2*int(a))

print("The solutions to the quadratic equation", a, "x2 +",  b, "x +", c, "= 0 are", sol_1, sol_2)

print("program ends")
