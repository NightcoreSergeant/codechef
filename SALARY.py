for i in range(int(input())):
    n=int(input())
    w=sorted(list(map(int,input().split())))
    c=0
    for i in range(n-1,0,-1):
        c+=w[i]-w[0]
    print(c)
    