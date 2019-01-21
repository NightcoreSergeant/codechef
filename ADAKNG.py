for i in range(int(input())):
    r,c,k=map(int,input().split())
    ans=9
    if r==1 and c==1 or r==1 and c==8 or r==8 and c==1 or r==8 and c==8:
        ans=4
    elif r==1 or c==1 or r==8 or c==8:
        ans=6
    print(ans)


