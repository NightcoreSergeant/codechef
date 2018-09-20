#for i in range(int(input())):
#    i,k = map(int,input().split())
#    a = 0
#    for i in input().split():
#        a += int(i)
#    print('even' if a%2==1 or a%2==0 and k > 1 else 'odd')
for i in range(int(input())):
    i,k = map(int,input().split())
    a = sum(map(int,input().split()))
    print('odd' if k == 1 and not a else 'even')
