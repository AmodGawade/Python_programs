#!/Users/amod/venv/bin/python

# Author name : Amod Gawade
# Date : 20 march 2020

# Asking input from user
string = input("Enter a word : ")

# Removing vowels
if string == 'x':
    exit()
else:
    new_string = string
    print("Removing vowels from the given string")
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in string.lower():
        if x in vowels:
            new_string = new_string.replace(x, "")
    print(new_string)

