#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    # Write your code here
    j = 0
    if n == 1:
        return 'Richard'
    while n != 1:
        if math.log(n,2) % 2 != 0.0 and math.log(n,2) % 2 != 1.0 :
            pot = 0
            while (2 ** pot < n):
                pot += 1
            n  -= (2 ** (pot -1))
        else:
            n /= 2
        j += 1    
    return 'Richard' if j % 2 == 0 else 'Louise'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
