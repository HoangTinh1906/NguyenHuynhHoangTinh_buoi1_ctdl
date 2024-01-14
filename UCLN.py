def UCLN(a,b):
    while a!=b:
        if a>b: 
            a=a-b
        else: 
            b=b-a
    return a
x=UCLN(2,2)
print(x)