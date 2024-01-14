def LuyThua(x,n):
    if n==0:
        return 1
    else:
        return x * LuyThua(x,n-1)
a=LuyThua(2,4)
print(a)