from math import sqrt
def nthFib(n):
    res = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
    print(int(res),'is',str(n)+'th fibonacci number')
nthFib(12)