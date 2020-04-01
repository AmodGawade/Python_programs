#!/Users/amod/venv/bin/python

# Author name : Amod Gawade
# Date : 31 march 2020

'''
for i in range(0, a):
    if i > 5:
        pass
    print(i)
print("am  out of loop statement")


i = 6
while i > 5:
    i = int(input("input me"))
    print(i)

i = 0
while True:
    i += 1
    if i == 10:
        break
    print("true")
'''
while True:
    i = int(input("input me"))
    a = oct(i)
    if a == 0o231:
        print("Escape key pressed")