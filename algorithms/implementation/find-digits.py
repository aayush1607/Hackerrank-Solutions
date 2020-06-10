#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    a=n
    k=0
    while(n>0):
        b=n%10
        if(b==0):
            n=n//10
            continue
        if(a%b==0):
            k+=1
        n=n//10
    return(k)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

