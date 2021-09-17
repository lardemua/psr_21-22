import math


def getDividers(value):
    """ Returns a list of dividers for number value.
    :param value:  the number for which to cimpute the dividers.
    :return: the list of dividers
    """
    dividers = []
    for i in range(1, int(round(math.sqrt(value)))):  # iterate from 1 to the number before value
        if (value % i) == 0:  # it could be better to replace by not (value%i)
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
