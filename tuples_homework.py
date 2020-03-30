#!/Users/amod/venv/bin/python
#Date : 27march
#In this program the user inputs 10 times and it calculates how many numbers and words are entered

a = input("type anything")
b = input("type anything")
c = input("type anything")
d = input("type anything")
e = input("type anything")
f = input("type anything")
g = input("type anything")
h = input("type anything")
i = input("type anything")
j = input("type anything")

tuple = (a, b, c, d, e, f, g, h, i, j)

num = [i for i in tuple if i.isdigit()]
str = [i for i in tuple if i.isalpha()]

print("the number of numbers you entered are ", len(num))
print("The number of words you entered are", len(str))


