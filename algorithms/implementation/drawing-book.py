#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if n%2==0:
        if p==n:
            return(0)
    elif p==n-1:
        return(0)
    if p==1:
        return(0)
    if p<=n//2:
        k=1
        while k!=p:
            k+=1
        return (int(k/2))
    else:
        k=n
        c=1
        while k!=p:
            k-=1
            c+=1
        return (int(c/2))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

