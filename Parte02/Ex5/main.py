#!/usr/bin/env python
# --------------------------------------------------
# A simple python script to print hello world!
# Miguel Riem Oliveira.
# PARI, Setember 2020.
# --------------------------------------------------
from copy import deepcopy


def countNumbersUpTo(stop_char):
    """
    Pythonic version!
    :param stop_char:
    :return:
    """
    inputs = []

    while True:
        char = raw_input('Enter a char (press ' + stop_char + ' to finish):')
        if char == 'X':
            break
        else:
            inputs.append(char)

    print('Here is the list of all your inputs: ' + str(inputs))

    # Ex 5a Processing of list of inputs
    total_numerics = 0
    for input in inputs:
        if input.isdigit():
            total_numerics += 1
    print('Total numeric inputs is ' + str(total_numerics))

    # Ex 5b
    numeric_inputs = []
    for input in inputs:
        if input.isdigit():
            numeric_inputs.append(int(input))  # add new element to list

    print('Numeric inputs:' + str(numeric_inputs))

    # Ex 5c
    dict_other = {}
    for idx, input in enumerate(inputs):
        if not input.isdigit():
            dict_other[str(idx)] = input  # add new key-value to dictionary

    print('dict_other:' + str(dict_other))

    # Ex 5d
    sorted_numeric_inputs = deepcopy(numeric_inputs)
    # sorted_numeric_inputs = numeric_inputs
    sorted_numeric_inputs.sort()
    print('sorted numeric inputs: ' + str(sorted_numeric_inputs))

    print('numeric inputs (again): ' + str(numeric_inputs))


def main():
    # ex4 a)
    # char = raw_input('Enter a char:')
    # print('You have entered  ' + char)
    # printAllCharsUpTo(char)

    # ex4 b)
    # readAllUpTo('X')

    # ex4 c)
    countNumbersUpTo('X')


if __name__ == '__main__':
    main()
