
'''
keywords - (Reserved Words).. built-in prg purpose

pass keyword

if <<condition>:  a < 10:
    pass
elif  <<condition>>: a > 10:
        a = a* 2 / 5 /10
else:
    statements

if
    else
    while
        continue
        break

    ========

    Data Types


    10  - 10Base - integer
    10.5 - floating point number -- float
    A  - letter - Character (Single Character)
    AMD   - Word -  String
    hello world  - Words - Strings

    int
    float
    str

    =  - single equal  is assignment o

    perator

    left side variable = right side value




    j = 10
    what is j has ?
        j has value 10


    j = 10   - valid
    k = 10.5 - valid
    if = 10  --invalid

    _amod = 10      - valid
    amod gawade = 100   - invalid
    amod_gawade = 100  - valid

    _gawade = 200  - valid
    1 = 100 invalid

    a-zA-Z0-9_

   amod = 100
   Amod = 200
   AMOD = 300

   case-senitive   --- sensitive --  a or A

   amod_1_gawade = 100
   Amod_1_gawade = 200

    gawade = 10
    gawade1 = 200.5
    gawade2 = 'Amod Gawade is 1000 learning python first time'
    gawade3 = "Amod Gawade"

    # C programm
    int gawade = 10
    float gawade1 = 200.5
    char gawade3 = "Amod Gawade"

Memory Management


Random Access memory (RAM)
Sgtorage (Static)

1000 1001 1002 1003 1004 1005   (2GB)
[20]  [200.5]      ['Amod Gwarde']  []  []      []

gawade = 10
gwade = [1000]
10
gawade = 20
gawade =[1000]
20

Strings
========
a = 'Amod Gawade'

Combination of Characters

first_string = "AMOD GAWADE"
print(first_string)

# Position - Index number -- 0,1 2,3,.....etc
# A      M       O         D       G      A    W   A   D   E
# 0     1       2          3    4   5      6    7   8   9   10

[AMOD GAWADE]
[0,1,2,3,4,5,6,7,8,9,10]

Which position D is there : 3
What is value of post 8 : A

String / Charactger Slicing

[0,1,2,3]
[AMOD]
[]
------
# Conditional Operator
== - whether it equal ?
<
<=
>
>=
!=

lefside value   operator  right side value

a= 10
b=20

a == b ?
a < b ?
a <= b?

if condition:
    statements


if condition:
    "True Statements"
else:
    "False Statements"

person1 = "Amod Gawade"
person2 = "Ankush Gawade"

a = 10
b = 20

c = a + b
d = a - b

if c >= b:
    print(person1)
    if condition:
        statement
    else:
        staqtement

else:
    print(person2)
    if condition:
        statement
    else:
        sgtatement


======

if condition:
    statement
elif conditon:
    statement
elif conditoin:
    statement
else:
    statements

-----
S.No| Name|Eng|Math|Sci
  1 | Amod|89 | 92 | 88
  2 | Amo1|87 | 90  | 98
  3 | Amo2| 90 | 65 | 40

Arithmetic Operators

+	Addition	x + y
-	Subtraction	x - y
*	Multiplication	x * y
/	Division	x / y
%	Modulus	x % y
**	Exponentiation	x ** y
//	Floor division	x // y 

Assignments Operators

=	x = 5	x = 5
+=	x += 3	x = x + 3
-=	x -= 3	x = x - 3
*=	x *= 3	x = x * 3
/=	x /= 3	x = x / 3
%=	x %= 3	x = x % 3
//=	x //= 3	x = x // 3
**=	x **= 3	x = x ** 3

Comparision Oeprators
==	Equal	x == y
!=	Not equal	x != y
>	Greater than	x > y
<	Less than	x < y
>=	Greater than or equal to	x >= y
<=	Less than or equal to	x <= y 

Logical Operations

and 	Returns True if both statements are true	x < 5 and  x < 10
or	    Returns True if one of the statements is true	x < 5 or x < 4
not	    Reverse the result, returns False if the result is true	not(x < 5 and x < 10) 

Identity Operator

is 	Returns True if both variables are the same object	x is y 

is not	Returns True if both variables are not the same object	x is not y 

in
not in

c = ['Amod Gawade']
a = 'G'
my question in a in c ? True
my another question in not a in c ? False

Looping Statements
For loop
source = [0,1,2,3,4,5,6,7,8,9,10]
for x in source:
    print(x)


functions:
its block of statemetns which repeats

def <<functionname>>():
    statements
PEP-8 function


# function takes argument

def add(a,b):
   print(a+b)

a = 10
b = 20

add(a,b)

-----
# function returs as well

def add(a,b):
   c = a + b
   return c


c = add(a,b)
print(c)


Exception Handling
-------------------------------
Whenever program gets an mal funt error which needs tob e handled correctly

try:
    statemetns

except IOError:
    print("You have to enter only numberic values")

except ValueError:
    print("Numbers accepted")

except Exception as e:
    print(e)


Modules
----------
Moduels is a another python program. you can import the existing python program to your program which is called modules

Program A  (file1.py)
  func1
  func2

#python3 file.1py


import file1
New Program B  (file2.py)
  func3
  func4
# main program
func3
fun4

Boiler plate


File Handling

OS  many type of files

file which contianers ASCII, text, bin, other formats

*.txt
*.log
*.bin
*.pdf
*.jpg
*.tiff
*.png

Operations
1. Open a file
2. Read / Writefrom or to a file
3. Close the file

Opening type
Read only
Read Write
Write Mode
Read binary
Append Mode

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)




f = open("filename.txt")
f.read()
f.close()

f = oepn("writefiele.txt","w")
f.write()
f.close()


f = open("filenae","rb")






































































'''
