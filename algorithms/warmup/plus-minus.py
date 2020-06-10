#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p,n,o=0,0,0
    for i in arr:
        if i>0:
            p+=1
        elif i<0:
            n+=1
        else:
            o+=1
    t=p+n+o
    P=float(p/t)
    N=float(n/t)
    O=float(o/t)
    print(P,N,O,sep='\n')

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

