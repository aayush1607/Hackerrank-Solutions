#!/bin/python3

import math
import os
import random
import re
import sys

def binarySearch(arr,val, start, end): 
    if start == end: 
        if arr[start] > val: 
            return start 
        else: 
            return start+1
    if start > end: 
        return start 
  
    mid = (start+end)//2
    if arr[mid] < val: 
        return binarySearch(arr, val, mid+1, end) 
    elif arr[mid] > val: 
        return binarySearch(arr, val, start, mid-1) 
    else: 
        return mid+1
     


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(s, a):
    s=set(s)
    s=list(s)
    s.sort()
    print(s)
    r=[]
    for j in range(len(a)):
        r.append(len(s)-binarySearch(s,a[j],0,len(s)-1)+1)
                    
    return (r)
    





        
        


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

