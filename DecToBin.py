def DecToBin(n):
    if n==0:
        return 0
    else:
       return n%2 +10*DecToBin(n//2)
def printDecToBin(n):
    if n==0:
        print(0)
    else:
        bin=DecToBin(n)
        print(bin)
printDecToBin(10)