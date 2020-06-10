#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    m=-1
    k=0
    for i in range(len(topic)):
        for j in range(i+1,len(topic)):
            b=bin(topic[i]|topic[j])
            if(str(b[2:]).count('1')>m):
                m=str(b[2:]).count('1')
                k=0
            elif(str(b[2:]).count('1')==m):
                k+=1
    return [m,k+1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = (int(input(),2))
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

