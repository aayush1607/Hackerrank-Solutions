

# Complete the solve function below.
def solve(s):
    s=s[0].upper()+s[1:]
    print(s)
    for i in range(len(s)):
        if s[i]==' ':
            s=s[:i+1]+s[i+1].upper()+s[i+2:]
            print(s)
    return s



