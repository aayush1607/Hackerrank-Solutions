def is_leap(year):
    if 1900<=year<=100000:
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    leap=True
                else:
                    leap=False
            else:
                leap=True
        else:
            leap=False
    else:
        pass
    
    
    
    return leap


