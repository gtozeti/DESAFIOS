#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    frase = s.replace(" ","").lower()
    alfa = 'abcdefghijklmnopqrstuvwyxz'
    
    
    for letra in frase:
        alfa = alfa.replace(letra,"")
        
    if len(alfa) > 0:
        return 'not pangram'
    else:
        return 'pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
