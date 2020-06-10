#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    d={}
    for i in range(26):
        D={chr(97+i):h[i]}
        d.update(D)
    m=d[word[0]]
    for i in d:
        if i in word:
            if d[i]>m:
                m=d[i]
    ans=m*len(word)
    return ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()

