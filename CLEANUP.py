for i in range(int(input())):
    n,m=map(int,input().split())
    l=tuple(map(int,input().split()))
    todo=[i for i in range(1,n+1) if i not in l]
    c=[]
    a=[]
    b=0
    for i in range(len(todo)):
        if b%2==0:
            c.append(todo[i])
        elif b%2==1:
            a.append(todo[i])
        b+=1
    print(*c)
    print(*a)