#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    n = int(len(matrix) / 2)
    coringa = list()
    aux = list()

    for i in range(0, n):
        for j in range(0,n):
            coringa.append(matrix[i][j])
            coringa.append(matrix[i][(2*n-1)-j])
            coringa.append(matrix[(2*n-1)-i][j])
            coringa.append(matrix[(2*n-1)-i][(2*n-1)-j])
            aux.append(max(coringa))
            coringa.clear()
            
    return sum(aux)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
