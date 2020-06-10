#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    l=[0]*k
    for i in range(n):
        l[s[i]%k]+=1
    if(l[0]>1):
        l[0]=1
    if(k%2==0):
        if(l[k//2]>1):
            l[k//2]=1
    
    a=l[0]
    print(list(map(int,"0123456")))
    print(l)
    for i in range(1,k//2+1):
        a+=max(l[i],l[k-i])
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()

