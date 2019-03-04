for i in range(int(input())):
    a=int(input())
    i=s=0
    mx=0
    ans=[0,0]
    while True:
        s+=a-2**i
        if s<=0:
            ans[0]=i
            break
        if s>mx:
            mx=s
            ans[1]=i+1
        i+=1
    print(*ans)