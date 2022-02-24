#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    r=[]
    n=re.split(r'(\s+)',s)
    for i in range(len(n)):
        r.append(str(n[i]).capitalize())
    return ''.join(str(ele) for ele in r)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
