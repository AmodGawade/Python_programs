#!/Users/amod/venv/bin/python
#name:Amod
#date:26march2020
#this program is for identifying the tallest student

student1 = input('Name of first student')
h1 = input('their height')

student2 = input('Name of second student')
h2 = input('Their height')

student3 = input('Name of the second student')
h3 = input('Their height')

student4 = input('Name of the fourth student')
h4 = input('Their height')

student5 = input('Name of the fifth student')
h5 = input("their height")

if h1 > h2 and h1 > h3 and h1 > h4 and h1 > h5:
    print('Student one is the tallest')
elif h2 > h1 and h2 > h3 and h2 > h4 and h2 > h5:
    print('Student two is the tallest')
elif h3 > h1 and h3 > h2 and h3 > h4 and h3 > h5:
    print('Student three is the tallest')
elif h4 > h1 and h4 > h2 and h4 > h3 and h4 > h5:
    print('Student four is the tallest')
elif h5 > h1 and h5 > h2 and h5 > h3 and h5 > h4:
    print('Student five is the tallest')
else:
    print('All students have same height')
