#!/Users/amod/venv/bin/python
#Date: 27march 2020
# this program takes inputs fom the user and sorts them into numbers and strings
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

print(num)
print(str)