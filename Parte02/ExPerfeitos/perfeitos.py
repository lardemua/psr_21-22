#!/usr/bin/env python

# Miguel Riem Oliveira
# PARI

maximum_number = 100


def getDividers(value):
    """ Returns a list of dividers for number value.
    :param value:  the number for which to cimpute the dividers.
    :return: the list of dividers
    """
    dividers = []
    for i in range(1, value):  # iterate from 1 to the number before value
        if (value % i) == 0: # it could be better to replace by not (value%i)
            dividers.append(i)

    return dividers


def isPerfect(value):
    """ ...
    :param value:
    :return:
    """
    dividers = getDividers(value)
    print('Number ' + str(value) + ' has dividers: ' + str(dividers))

    if not dividers:  # if list is empty assume number is not perfect
        return False

    if sum(dividers) == value:
        return True
    else:
        return False


def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()
