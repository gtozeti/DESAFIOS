#!/bin/python3

import math
import os
import random
import re
import sys
import datetime
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    periodo = s.split(s[:-2])[1]
    valores = s.split(s[-2])[0]
    hora = f'{valores} {periodo}'
    hora12 = datetime.datetime.strptime(hora, '%I:%M:%S %p')
    hora24 = datetime.datetime.strftime(hora12, '%H:%M:%S')  
    return hora24


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
