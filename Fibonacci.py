#!/Users/amod/venv/bin/python

# Author name : Amod Gawade
# Date : 20 march 2020

# Asking user for input
num = int(input("Enter how many fibonnaci numbers you would like : "))
a = 0
b = 1
fib_list = []

# taking previous number and adding 2nd previous number to it
for i in range(0, num):
    c = a + b
    a = b
    b = c
    fib_list.append(b)
    print(b)
print(fib_list)
