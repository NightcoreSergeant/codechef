import math
for i in range(int(input())):
    n=int(input())
    m=n-1
    for i in range(1,int(math.sqrt(n))+1):
        if n%i!=0:
            continue
        elif m>abs(i-n//i):
            m=abs(i-n//i)
    print(m)