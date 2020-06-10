#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(s):
    h,l=s[0],s[0]
    hk=0
    lk=0
    for i in range(1,len(s)):
        if(s[i]>h):
            h=s[i]
            hk+=1
        if(s[i]<l):
            l=s[i]
            lk+=1
    j=[hk,lk]
    return(j)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

