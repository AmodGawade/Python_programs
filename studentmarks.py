#!/Users/amod/venv/bin/python
#Name:Amod
#Date:25march2020
#this program is used to identify which student has the greatest marks out of 5

#to get input from user:
student1 = input('The name of student one is___')
oneeng = input('Their marks in english are___')
onemath = input('Their marks in maths is ___')
onescience = input('Their marks in science is___')

student2 = input('The name of student two is___')
twoeng = input('Their marks in english are___')
twomath = input('Their marks in maths is ___')
twoscience = input('Their marks in science is___')

student3 = input('The name of student three is___')
threeeng = input('Their marks in english are___')
threemath = input('Their marks in maths is ___')
threescience = input('Their marks in science is___')

student4 = input('The name of student four is___')
foureng = input('Their marks in english are___')
fourmath = input('Their marks in maths is ___')
fourscience = input('Their marks in science is___')

student5 = input('The name of student 5 is___')
fiveeng = input('Their marks in english are___')
fivemath = input('Their marks in maths is ___')
fivescience = input('Their marks in science is___')

if oneeng > twoeng and oneeng > threeeng and oneeng > foureng and oneeng > fiveeng:
    print('student one has greatest marks in english')
elif twoeng > oneeng and twoeng > threeeng and twoeng > foureng and twoeng > fiveeng:
    print('student two has greatest marks in english')
elif threeeng > oneeng and threeeng > twoeng and threeeng > foureng and threeeng > fiveeng:
    print('student three has greatest marks in english')
elif foureng > oneeng and foureng > twoeng and foureng > threeeng and foureng > fiveeng:
    print('student four has greatest marks in english')
elif fiveeng > oneeng and fiveeng > twoeng and fiveeng > threeeng and fiveeng > foureng:
    print('student five has greatest marks in english')
else:
    print('all students have equal marks in english')

if onemath > twomath and onemath > threemath and onemath > fourmath and onemath > fivemath:
    print('student one has greatest marks in math')
elif twomath > onemath and twomath > threemath and twomath > fourmath and twomath > fivemath:
    print('student two has greatest marks in math')
elif threemath > onemath and threemath > twomath and threemath > fourmath and threemath > fivemath:
    print('student three has greatest marks in math')
elif foureng > onemath and fourmath > twomath and fourmath > threemath and fourmath > fivemath:
    print('student four has greatest marks in math')
elif fivemath > onemath and fivemath > twomath and fivemath > threemath and fivemath > fourmath:
    print('student five has greatest marks in math')
else:
    print('all students have equal marks in math')

if onescience > twoscience and onescience > threescience and onescience > fourscience and onescience> fivescience:
    print('student one has greatest marks in science')
elif twoscience > onescience and twoscience> threescience and twoscience > fourscience and twoscience > fivescience:
    print('student two has greatest marks in science')
elif threescience > onescience and threescience > twoscience and threescience > fourscience and threescience > fivescience:
    print('student three has greatest marks in science')
elif fourscience > onescience and fourscience > twoscience and fourscience > threescience and fourscience > fivescience:
    print('student four has greatest marks in science')
elif fivescience > onescience and fivescience> twoscience and fivescience > threescience and fivescience > fourscience:
    print('student five has greatest marks in science')
else:
    print('all students have equal marks in science')
