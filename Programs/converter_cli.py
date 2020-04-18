#!/Users/amod/venv/bin/python
# name : Amod
# date : 1 april 2020
import argparse


# Functions are defined:
# convert celsius to fahrenheit
def temp(a):
    b = (float(a)*9/5) + 32
    print("The value of temperature in fahrenheit is", b)
    return b


# hours to seconds
def time(a):
    b = float(a)*3600
    print("The value of time in seconds is", b)
    return b


# kilometers/h to miles/h
def speed(a):
    b = float(a)/1.609
    print("The value of speed in miles per hour is", b)
    return b


# convert kg to lbs
def mass(a):
    b = float(a)/0.45359237
    print("The value of mass in pounds is", b)
    return b


# convert litres to gallon
def vol(a):
    b = float(a)/3.785
    print("The value of volume in gallons is", b)
    return b


# convert cm to inch
def length(a):
    b = float(a)/2.54
    print("The value of length in inches is", b)
    return b


# convert horsepower to kilowatts
def power(a):
    b = float(a)*1.36
    print("The value of power in kilowatts is", b)
    return b


# convert degree to radians
def arc(a):
    b = float(a)*57.2957795131
    print("The value of angle in radians is", b)


# convert sqm to acre
def area(a):
    b = float(a)*4047
    print("The value of area in acres is", b)


# convert joules to electron volts
def energy(a):
    b = float(a)*1.6*(10**-19)
    print("The value of energy in eV is", b)

parser = argparse.ArgumentParser(description="Converts units ", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-m', type=str, help='''Measurements to Convert
    To convert celsius to fahrenheit type 'temp' 
    To convert hours to seconds type 'time'
    To convert kilometres per hour to miles per hour type 'speed'
    To convert kilograms to pounds type 'mass'
    To convert litres to gallons type 'vol'
    To convert cm to inch type'length'
    To convert horsepower to kilowatts type 'power'
    To convert degree to radians type 'arc'
    To convert metres square to acre type 'area'
    To convert joules to electron volts type 'energy' ''')
parser.add_argument('-v', help="Metrics Value to Convert")
args = parser.parse_args()
op = args.m
c = args.v

# main program
def convert():
    print("This program is used to convert units")

    """ op = input('''To convert celsius to fahrenheit type 'temp'
    To convert hours to seconds type 'time'
    To convert kilometres per hour to miles per hour type 'speed'
    To convert kilograms to pounds type 'mass'
    To convert litres to gallons type 'vol'
    To convert cm to inch type'length'
    To convert horsepower to kilowatts type 'power'
    To convert degree to radians type 'arc'
    To convert metres square to acre type 'area'
    To convert joules to electron volts type 'energy' 
    Enter your choice : ''')  """

    try :
        if op == 'temp':
            #c = input("Enter the temperature in celsius : ")
            temp(c)
        elif op == 'time':
            #c = input("Enter the time in hours : ")
            time(c)
        elif op == 'speed':
            #c = input("Enter the speed in kilometers per hour : ")
            speed(c)
        elif op == 'mass':
            #c = input("Enter the mass in kilograms")
            mass(c)
        elif op == 'vol':
            #c = input("Enter the volume in litres")
            vol(c)
        elif op == 'length':
            #c = input("Enter the length in centimeters")
            length(c)
        elif op == 'power':
            #c = input("Enter the power in horsepower")
            power(c)
        elif op == 'arc':
            #c = input("Enter the angle in degrees")
            arc(c)
        elif op == 'area':
            #c = input("Enter the area in square metres")
            area(c)
        elif op == 'energy':
            #c = input("Enter the energy in joules")
            energy(c)
        else:
            print("Incorrect words typed.")
    except ValueError:
        print("Incorrect value entered. Must be numeric")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    convert()
