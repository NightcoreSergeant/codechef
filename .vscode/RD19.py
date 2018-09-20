def c(a,i):
    for j in range(len(a)):
        if gcd(a[i],a[j]) != 1 and i != j:
            a.pop(i)
    return a
from math import gcd
for i in range(int(input())):
    c = 0
    a = list(map(int,input().split()))
    for i in range(int(input())):
        try:
            c(a,i)
        except:
            break
    print(a)