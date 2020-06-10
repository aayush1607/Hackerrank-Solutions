def count_substring(string, sub):
    subs=len(sub)
    s=len(string)
    c=0
    j=0
    while j<s:
        if string[j:j+subs]==sub:
            c=c+1
        j+=1
    return c


