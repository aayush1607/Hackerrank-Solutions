#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    k,j=0,0
    j+=c.count(1)
    for i in range(len(c)):
        if(c[i]!=1):
            k+=1
        else:
            j+=(k//2)
            k=0
    j+=(k//2)
    return j

        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

