#!/Users/amod/venv/bin/python
# name : Amod


def add(a, b):
    print(a+b)


def sub(x, y):
    '''doc string
    this method is subtraction
    it takes argument x, y
    '''
    c = x - y
    print(c)


def main():
    a = 10
    b = 20
    add(a, b)
    sub(a, b)


# Boiler Plate
if __name__ == '__main__':
    main()
