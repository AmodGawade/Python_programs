#!/Users/amod/venv/bin/python

# Author name : Amod Gawade
# Date : 20 march 2020

# Asking user for input
num_of_nums = int(input("Enter how many numbers to check : "))
num = []
for i in range(0, num_of_nums):
    num.append(int(input("Type some number")))

# Printing all the negative numbers
neg_numbers = []
for x in num:
    if x < 0:
        print(x)
        neg_numbers.append(x)
if neg_numbers:
    print(neg_numbers)
else:
    print("No negative numbers entered")

