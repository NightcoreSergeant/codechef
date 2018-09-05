from math import gcd
for i in range(int(input())):
    x = list(map(int,input().split()))
    x = x[1:]
    g = gcd(x[0],x[1])
    for i in range(2,len(x)):
        g = gcd(g, x[i])
    if g == 1:
        print(*x)
    else:
        for i in range(len(x)):
            x[i] //= g
        print(*x)
