for i in range(int(input())):
    n,k,v=map(int,input().split())
    a=list(map(int,input().split()))
    x=(v*n+v*k-sum(a))
    if x%k==0 and x>0:
        print(x//k)
    else:print(-1)