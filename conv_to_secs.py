#!/Users/amod/venv/bin/python

# Author Name : Amod gawade
# Date : 20 march 2020

# Requesting input fro user
h = input("Enter the number of hours : ")
m = input("Enter the number of minutes : ")
s = input("Enter the number of seconds : ")

# calculating seconds
# Multiplying h into 3600 and minutes into 60 and adding
t = int(h)*3600 + int(m)*60 + int(s)
print("The total time in seconds is", t)
