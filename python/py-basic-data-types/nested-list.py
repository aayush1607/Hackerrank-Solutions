n=int(input())
l=[]
for i in range(n):
    name=input()
    mark=float(input())
    d=[mark,name]
    l.append(d)
s=set()
for i in l:
    s.add(i[0])
w=list(s)
w.sort()
rp=w[1]
g=[]
for i in range(len(l)-1,-1,-1):
    if l[i][0]==rp:
        g.append(l[i][1]) 
g.sort()
for i in g:
    print(i)






