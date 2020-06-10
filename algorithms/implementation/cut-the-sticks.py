#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def c(arr):
    k=1
    for i in range(len(arr)):
        if arr[0]!=arr[i]:
            k=0
    if k==0:
        return False
    else:
        return True
def cutTheSticks(arr):
    l=[len(arr)]
    f=[]
    m=min(arr)
    if(c(arr)):
        return l
    while(True):
        for i in arr:
            if((i-m)!=0):
                f.append(i-m)
        if(c(f)==True):
            l.append(len(f))
            break
        else:
            l.append(len(f))
            m=min(f)
            arr.clear()
            arr=f.copy()
            f.clear()
            continue
    return l

    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

