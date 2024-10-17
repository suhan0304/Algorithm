#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    ans = [0, 0, 0]

    for i in range(n) :
        if arr[i] > 0 :
            ans[0] += 1
        elif arr[i] < 0 :
            ans[1] += 1
        else :
            ans[2] += 1
    
    for a in ans :
        print("{:.6f}".format(a/n))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
