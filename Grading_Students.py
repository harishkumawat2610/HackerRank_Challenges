#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    hk=[]
    for i in grades:
        if i < 38:
            hk.append(i)
        elif i >= 38:
            val= i//5 + 1
            dup_val = 5*val
            check = dup_val - i
            if check < 3:
                 hk.append(dup_val)
            else:
                hk.append(i)
    return hk

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
