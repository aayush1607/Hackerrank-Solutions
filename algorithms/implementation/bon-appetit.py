#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    billsum=sum(bill)
    finalbill=billsum-bill[k]
    if(finalbill//2==b):
        print("Bon Appetit")
    else:
        print(abs(finalbill//2-b))


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

