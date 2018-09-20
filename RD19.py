#for i in range(int(input())):
#    input()
#    a = list(map(int,input().split()))
#    for i in a[1:]:
#        while i:
#            a[0], i = i, a[0]%i
#            print(a[0],i)
#    print(0 if a[0] == 1 else -1)
from math import gcd
for i in range(int(input())):
    input()
    a = list(map(int,input().split()))
    for i in a[1:]:
        a[0] = gcd(a[0],i)
        if a[0] == 1: #once one = always one :)
            break
    print(0 if a[0] == 1 else -1)
        
