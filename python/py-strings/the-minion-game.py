import string
def minion_game(s):
    # your code goes here
    c=string.ascii_uppercase
    v="AEIOU"
    c=list(c)
    v=list(v)
    for i in v:
        c.remove(i)

    stu=0
    kev=0
    for i in range(len(s)):
        if(s[i] in v):
            kev+=len(s)-i
        else:
            stu+=len(s)-i
    if(stu>kev):
        st="Stuart "+str(stu)
    elif(stu<kev):
        st="Kevin "+str(kev)
    else:
        st="Draw"
    print(st)




