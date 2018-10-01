for i in range(int(input())):
    c1=0
    c2=0
    n,k=map(int,input().split())
    for i in input():
        if i.isupper():
            c1+=1
        else:
            c2+=1
    if c1 <= k and c1 <= k:
        print('both')
    elif c1 <= k:
        print('chef')
    elif c2 <= k:
        print('brother')
    else:
        print('none')