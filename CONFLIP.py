for i in range(int(input())):
    for i in range(int(input())):
        s,n,q=map(int,input().split())
        if s!=q and n%2==1:
            n//=2
            n+=1
        else:
            n//=2
        print(n)