for i in range(int(input())):
    input()
    l=list(map(int,input().split()))
    k=l[int(input())-1]
    l.sort()
    for i in range(len(l)):
        if k==l[i]:
            break
    print(i+1)
