def merge_the_tools(s, k):
    # your code goes here
    i=iter(s)
    l=(list(zip(*[i]*k)))
    for i in range(len(l)):
        t=list(l[i])
        t=list(dict.fromkeys(t))
        l[i]="".join(t)
    for i in l:
        print(i)




    


