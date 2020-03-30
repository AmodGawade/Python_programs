#!/Users/amod/venv/bin/python
import cmath
# Author name : Amod Gawade
# Date : 30 March 2020

print("Program starts")

# Asking user for inputs
a = input("Enter a value for one side of the triangle : ")
b = input("Enter a value for the second side of the triangle : ")
c = input("Enter a value for the third side of the triangle : ")

# Calculating the area:
s = (int(a) + int(b) + int(c))/2
area = cmath.sqrt((s*(s-int(a))*(s-int(b))*(s-int(c))))
print("The area of the triangle is", area)

print("Program ends")


