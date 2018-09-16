#for i in range(int(input())):
#    n = int(input())
#    l1 = [0,0]
#    l2 = [0,0]
#    l3 = [0,0]
#    for i in range(n):
#        c,l,x = map(int,input().split())
#        if l== 1 and l1[0] <= x:
#            if l1[0] == x and c < l1[1]:
#                l1[1] = c
#            elif l1[0] == x:
#                continue
#            else:
#                l1 = [x,c]
#        elif l==2 and l2[0] <=x:
#            if l2[0] == x and c < l2[1]:
#                l2[1] = c
#            elif l2[0] == x:
#                continue
#            else:
#                l2 = [x,c]
#        elif l==3 and l3[0] <=x:
#            if l3[0] == x and c < l3[1]:
#                l3[1] = c
#            elif l3[0] == x:
#                continue
#            else:
#                l3 = [x,c]
#    print('{}\n{}\n{}'.format(' '.join(map(str,l1)),' '.join(map(str,l2)),' '.join(map(str,l3))))
for i in range(int(input())):
    n = int(input())
    lll = [[0,0],[0,0],[0,0]]
    for i in range(n):
        c,i,x = map(int,input().split())
        if x>lll[i-1][0] or x == lll[i-1][0] and c < lll[i-1][1]:
            lll[i-1] = [x,c]
    for i in lll:
        print(*i)
