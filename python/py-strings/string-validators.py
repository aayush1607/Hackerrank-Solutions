if __name__ == '__main__':
    s = input()
    a=0
    b=0
    c=0
    d=0
    e=0
    for i in s:
        if(i.isalnum()):
            a=1
        if(i.isalpha()):
            b=1
        if(i.isdigit()):
            c=1
        if(i.islower()):
            d=1
        if(i.isupper()):
            e=1
    l=[a,b,c,d,e]
    for i in l:
        if(i==1):
            print("True")
        else:
            print("False")

