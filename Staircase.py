#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    k= n - 1
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for h in range(0,i+1):
            print("#",end="")
        print("\r")

if __name__ == '__main__':
    n = int(input())

    staircase(n)
