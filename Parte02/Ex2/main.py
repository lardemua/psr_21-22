#!/usr/bin/env python

# Miguel Riem Oliveira
# PARI

maximum_number = 100

# from my_functions import getDividers, isPerfect
# import my_functions
import my_functions as mf

# import outras_functions
# from teste_pasta.outras_functions import isPerfect
import teste_pasta.outras_functions as of

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if of.isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()
