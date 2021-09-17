#!/usr/bin/env python

# Miguel Riem Oliveira
# PARI
import argparse


from my_functions import getDividers, isPerfect

def main():

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-mn', '--max_number', type=int, default=20,
                        help='Max number to evaluate with isPerfect.')
    args = vars(parser.parse_args())
    print(args)

    maximum_number = args['max_number']

    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()
