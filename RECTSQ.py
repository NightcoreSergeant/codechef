from math import gcd
for i in range(int(input())):
    n, m=map(int,input().split())
    print((n*m)//gcd(n,m)**2)