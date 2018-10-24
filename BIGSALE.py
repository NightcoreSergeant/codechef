for i in range(int(input())):
    ans = 0
    for i in range(int(input())):
        a,b,c = map(int,input().split())
        o = a
        a += a*c*0.01
        a -= a*c*0.01
        ans += (o-a)*b
    print(ans)