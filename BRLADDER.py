for i in range(int(input())):
    a=sorted(map(int,input().split()))
    print('YES' if a[1]-a[0] == 2 or (a[0]==a[1]-1 and not a[0]-1 & 1) else 'NO')
