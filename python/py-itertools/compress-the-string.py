# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
i=0
while i<len(s):
    x=1
    p=i
    for j in range(i+1,len(s)):
        if s[j]==s[i]:
            p=j
            x+=1
        else:
            break
    print('('+str(x)+','+' '+s[i]+')',end=' ')
    i=p
    i+=1

