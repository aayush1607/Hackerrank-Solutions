#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    p=0
    for i in range(1,(max(b))+1):
        if max(b)%i==0:
            k=0
            for j in range(len(b)):
                if b[j]%i==0:
                    k+=1
            if k==len(b):
                g=0
                for c in range(len(a)):
                    if i%a[c]==0:
                        g+=1
                if g==len(a):
                    p+=1
    return p



    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

