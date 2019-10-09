#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    ali = 0
    bob = 0
    for (i,j) in zip (a,b):
        if i>j:
            ali=ali+1
        elif i == j:
            pass
        elif i<j:
            bob = bob + 1
    return [ali,bob]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
