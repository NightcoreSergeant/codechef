for i in range(int(input())):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    m=sum(l)
    if m%x>=min(l):
        print(-1)
    else:
        print(m//x)