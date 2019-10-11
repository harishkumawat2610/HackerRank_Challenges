#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    hk = arr
    hk.sort()
    mk = len(hk)
    min = 0
    max = 0
    for i in range(1, mk):
        max = max + hk[i]
    for j in range(0, mk - 1):
        min = min + hk[j]
    print(min, max)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
