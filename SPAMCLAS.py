def bla():
    for _ in range(int(input())):
        N,minX,maxX = map(int,input().split())
        e,o=0,1
        for _ in range(N):
            w,b=map(int,input().split())
            e=(w*e+b)%2
            o=(w*o+b)%2
    
        ans=0
        r=maxX-minX+1
    
        k=r/2
        if minX%2==0:
            k+=1
        l=r-k
        
        if e==0:
            ans+=k
        if o==0:
            ans+=l
        
        return '{} {}'.format(ans, r-ans)

print(bla())