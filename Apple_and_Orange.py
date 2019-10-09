#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ora = []
    app = []
    a = a
    b = b
    ap_count = 0
    or_count = 0
    for i in apples:
        ap = a + (i)
        app.append(ap)
    for j in oranges:
        ori = b + (j)
        ora.append(ori)
    for i in app:
        if i >= s and i <= t:
            ap_count = ap_count + 1
        else:
            pass
    for i in ora:
        if i >= s and i <= t:
            or_count = or_count + 1
        else:
            pass
    print(ap_count)
    print(or_count)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
