for i in range(int(input())):
    n,a,b=map(int,input().split())
    x = list(map(int,input().split()))
    print((x.count(a)/n)*(x.count(b)/n))
