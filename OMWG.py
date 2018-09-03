#for _ in range(int(input())):
#    n, m = map(int,input().split())
#    x1 = 0
#    x2 = 0
#    c = 0
#    if n > 2 and m > 2:    
#        if n % 3 == 0:    
#            x2 = n*2
#            x1 = n
#    
#        elif n % 3 == 1:    
#            x1 += 1 + n
#            x2 = n
#            x2 /= 2
#            x2 *= 3.5
#        else:
#            x1 += 2 + n
#            x2 = n
#            x2 //= 2
#            x2 *= 4
#    
#        for i in range(m):
#            if i > 1:
#                c += x2
#            else:
#                c += x1
#    
#    
#    
#    
for _ in range(int(input())):
    n, m = map(int,input().split())
    print(m*(n-1) + n*(m-1))