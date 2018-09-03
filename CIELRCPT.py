#for _ in range(int(input())):
#    x = [i for i in range(12)]
#    i = 11
#    p = int(input())
#    counter = 0
#    while p != 0:
#        if 2**x[i] <= p:
#            p -= 2**x[i]
#            counter += 1
#        else:
#            i -= 1
#        
#    print(counter)
#
#
#better one
for _ in range(int(input())):
    p = int(input())
    counter = 0
    for j in range(11,-1,-1):
        if p/(2**j) >= 1:
            counter += p//(2**j)
            p %=2**j
            if p == 0:
               break
    print(counter)