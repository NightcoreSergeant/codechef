for i in range(int(input())):
    l=list(map(int,input().split()))
    l.sort()
    if l[0]==l[1] and l[2]==l[3]:
        print('YES')
    else:
        print('NO')
