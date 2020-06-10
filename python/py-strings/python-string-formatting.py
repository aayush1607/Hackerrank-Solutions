def print_formatted(number):
    # your code goes here
    w=len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(w,' '),end=' ')
        o=str(oct(i))
        print(o[2:].rjust(w,' '),end=' ')
        h=str(hex(i))
        print(h[2:].rjust(w,' '),end=' ')
        b=str(bin(i))
        print(b[2:].rjust(w,' '),end=' ')
        print()


