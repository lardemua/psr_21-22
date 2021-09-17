#!/usr/bin/env python

def addComplex(x, y):
    x_r = x[0]
    x_i = x[1]

    y_r = y[0]
    y_i = y[1]

    # z = x + y
    z_r = x_r + y_r
    z_i = x_i + y_i

    return (z_r, z_i)


def multiplyComplex(x, y):
    x_r, x_i = x[0], x[1]
    y_r, y_i = y[0], y[1]

    z_r = x_r * y_r - x_i * y_i
    z_i = x_r * y_i + x_i * y_r

    return (z_r, z_i)

def printComplex(x):
    print('(' + str(x[0]) + ', ' + str(x[1]) + 'i)')


def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))


if __name__ == '__main__':
    main()
