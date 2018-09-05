for i in range(int(input())):
    n, b, m = map(int,input().split())
    time = 0
    while n != 1:
        if n%2==0:
            time+=(n//2)*m+b
            n//=2
        else:
            time+=((n+1)//2)*m+b
            n = n-(n+1)//2
        m*=2
    print(time+m)

