#!/usr/bin/env python
# from collections import namedtuple
# Complex = namedtuple('Complex', ['r', 'i'])

def addComplex(x, y):
    z_r = x['r'] + y['r']
    z_i = x['i'] + y['i']
    return Complex(r=z_r, i=z_i)


def multiplyComplex(x, y):
    x_r, x_i = x[0], x[1]
    y_r, y_i = y[0], y[1]

    z_r = x_r * y_r - x_i * y_i
    z_i = x_r * y_i + x_i * y_r

    return Complex(z_r, z_i)

class Complex:

    def __init__(self, r, i):
        self.r = r
        real = r
        self.i = i

    def __str__(self):
        return '(' + str(self.r) + ', ' + str(self.i) + 'i)'

    def addComplex(self, y):
        self.r += y.r
        self.i += y.i

def main():

    c1 = Complex(r=5, i=3)
    c2 = Complex(r=-2, i=7)

    print('Initial c1 ' + str(c1))
    print('Initial c2 ' + str(c2))
    c1.addComplex(c2)
    print('c1 after add ' + str(c1))


if __name__ == '__main__':
    main()
