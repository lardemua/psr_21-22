#!/usr/bin/env python


def isPrimeqqcoisa(value):
    # isto e um comentario

    for i in range(2, value):
        if not value % i:
            return False
    	
    return True

def main():
    
    maximum_number = 50
    print("Starting to compute prime numbers up to " + str(maximum_number))

    from colorama import Fore
    for i in range(0, maximum_number):
        if isPrimeqqcoisa(i):

            print('Number ' + Fore.RED + str(i) + Fore.RESET + ' is prime.')
        else:
            print('Number ' + str(i) + ' is not prime.')

if __name__ == "__main__":
    main()
