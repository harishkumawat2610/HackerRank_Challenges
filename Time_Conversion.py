#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:] == 'AM' and s[:2] == "12":
        return "00" + s[2:-2]
    elif s[-2:] =='AM':
        return s[:-2]
    elif s[-2:]=='PM' and s[:2] =="12":
        return s[:-2]
    else:
        return str(12 + int(s[:2]))+s[2:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
