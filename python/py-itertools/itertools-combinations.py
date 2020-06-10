# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s,k=input().split()
k=int(k)
s=list(s)
s.sort()
s="".join(s)
for i in range(1,k+1):
    l=list(combinations(s,i))
    for j in range(len(l)):
        print("".join(l[j]))



