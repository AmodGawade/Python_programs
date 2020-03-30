#!/Users/amod/venv/bin/python

# Author name : Amod Gawade
# Date : 20 March 2020

print("Program starts")

# Asking user how many inputs they want
a = input("Enter how many values to be in the list : ")
num = []
for i in range(0, int(a)):
    num1 = input("Enter a value : ")
    num.append(num1)

# Finding the greatest value in the list
max_method = int(max(num))
print("The largest number is %d (by max method)" % max_method)

num.sort()
sort_method = int(num[-1])
print("The largest number is %d (by sort method)" % sort_method)

print("program ends")






