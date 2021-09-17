#!/usr/bin/env python
# --------------------------------------------------
# Miguel Riem Oliveira.
# PARI, September 2020.
# --------------------------------------------------
import argparse
from functools import partial

import cv2
import numpy as np


def main():
    # declare function sum
    def sum_3_values(a, b, c):
        return (a + b + c)

    # declara a new function with 2 imput args using partial
    sum_2_values = partial(sum_3_values, c=0)

    # Use the function
    print(sum_3_values(3, 2, 5))

    # use the function with just 2 input args
    print(sum_3_values(3, 2, 0))
    print(sum_2_values(3, 2))


if __name__ == '__main__':
    main()
