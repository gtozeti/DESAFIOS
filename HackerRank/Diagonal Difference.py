#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    dP = 0
    dS = 0
    c = len(arr) - 1

    for numLinha, linha in enumerate(arr):
        for numColuna, coluna in enumerate(linha):
                if numLinha == numColuna:
                    dP += coluna
                if numColuna == c:
                    dS += coluna 
                    c -= 1

    return(abs(dP- dS))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
