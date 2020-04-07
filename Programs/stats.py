#!/Users/amod/venv/bin/python
# name : Amod
import statistics

input_list = []


def find_mean(x):
    a = statistics.mean(input_list)
    print("The mean is", a)


def find_median(y):
    b = statistics.median(input_list)
    print("The median is", b)


def find_mode(z):
    c = statistics.mode(input_list)
    print("The mode is", c)


d = input("How many numbers you would like to input : ")
for i in range(int(d)):
    e = input("Enter a value : ")
    input_list.append(int(e))

find_mean(input_list)
find_median(input_list)
find_mode(input_list)


