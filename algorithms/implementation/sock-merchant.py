#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d=dict()
    for i in range(n):
        if ar[i] in d:
            d[ar[i]]+=1
        else:
            d.update({ar[i]:1})
    p=0
    for i in d:
        print(i,d[i])
        p+=(d[i]//2)
    return(p)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

