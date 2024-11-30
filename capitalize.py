#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    list_s = s.split(' ')
    first_name = list_s[0]
    first_name = first_name.replace(first_name[0], first_name[0].upper())
    second_name = list_s[1]
    second_name = second_name.replace(second_name[0], second_name[0].upper())
    capitalized_s = first_name+' '+second_name
    return capitalized_s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

