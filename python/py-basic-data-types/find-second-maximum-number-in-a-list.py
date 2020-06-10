n = (input())
arr=[int(i) for i in input().split()]
arr.sort()
m=max(arr)
l=[]
for i in range(len(arr)):
    if arr[i]!=m:
        l.append(arr[i])
        
print(max(l))

    



