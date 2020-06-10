# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=[]
for i in range(n):
    p=input()
    l.append(p)
s=set(l)
cc=len(s)
print(cc)
for i in range(len(l)):
    c=1
    if l[i]==-1:
        continue
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            c+=1
            l[j]=-1
    print(c,end=' ')

