#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    frase = ''

    if k > len(alpha):
        k = k % 26
    trecho = alpha[:k]
    cipher = alpha.replace(trecho,'') + trecho

    for indice, x in enumerate(s):
        if x.isalpha():
            if x.islower():
                frase += cipher[alpha.index(x)]
            elif x.isupper():
                frase += cipher[alpha.index(x.lower())].upper()
        else:
            frase += x
    return frase
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
