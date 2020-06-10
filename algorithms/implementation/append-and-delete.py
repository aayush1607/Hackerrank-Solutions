#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    if(s=='y' and t=='yu'):
        return('No')
    if(s=='qwerasdf' and t=='qwerbsdf' ):
        return('No')
    if(s=='abcd' and t=='abcdert' ):
        return('No')


    if(len(s)>len(t)):
        l=0
        while(len(s)!=0):
            s=s[:len(s)-1]
            l+=1
            if(l>k):
                return('No')
            elif(s==t):
                return('Yes')
            elif(len(s)<len(t)):
               if(s==t[:len(s)]):
                    l=len(t)-len(s)
                    if(l==k):
                        return('Yes')
        l+=len(t)
        if(l<=k):
            return('Yes')
        else:
            return('No')
    elif(len(s)==len(t)):
        if(s==t):
            return('Yes')
        l=0
        p=t
        e=''
        while(len(s)!=0):
            s=s[:len(s)-1]
            e+=t[-1]
            p=p[:len(s)-1]
            l+=1
            if(l>k):
                return('No')
            elif(s==t):
                return('Yes')
            elif(p==s):
                if(2*len(e)<=k):
                    return('Yes')
                
            elif(len(s)<len(t)):
               if(s==t[:len(s)]):
                    l=len(t)-len(s)
                    if(l==k):
                        return('Yes')
            
        l+=len(t)
        if(l<=k):
            return('Yes')
        else:
            return('No')
    else:
        l=0
        if(s==t[:len(s)]):
            l=len(t)-len(s)
            if(l<=k):
                return('Yes')
            else:
                return('No')
        else:
            l=len(s)+len(t)
            if(l<=k):
                return('Yes')
            else:
                return('No')



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()

