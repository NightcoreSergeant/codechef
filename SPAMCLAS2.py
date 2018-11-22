for i in range(int(input())):
    n,minx,maxx=map(int,input().split())
    yes=no=0
    w=[]
    a=[]
    add=[]
    alw=1
    for i in range(n):
        l1,l2=map(int,input().split())
        w.append(l1%2)
        a.append(l2%2)
    for i in range(n-1,-1,-1):
        add.append(a[i] & alw)
        alw= alw & w[i]  
    
    if len(add)!=1:
        for i in range(1,len(add)):
            add[0]=add[i]^add[0]
    add=add[0]
    r=maxx-minx+1
    if alw==0 and add==0:
        no=r
    elif alw==0 and add==1: 
        yes=r
    elif r%2==0:
        yes=no=r//2
    elif minx%2==0 and add==1:
        no=r//2
        yes=r//2+1
    elif minx%2==0 and add==0:
        no=r//2+1
        yes=r//2   
    elif minx%2==1 and add==1:
        no=r//2+1
        yes=r//2
    elif minx%2==1 and add==0:
        no=r//2
        yes=r//2+1
    
    print(no,yes)