for i in range(int(input())):
    n,u,d=map(int,input().split())
    h=list(map(int,input().split()))
    p=True
    for i in range(1,n):
        if h[i]-h[i-1]<=u and h[i-1]<=h[i] or h[i-1]-h[i]<=d and h[i-1]>=h[i]:
            continue
        elif p and h[i-1]>h[i]:
            p = False
        else:
            break
    if i == n-1:
        i+=1
    print(i)

#for i in range(int(input())):
#    n,u,d=map(int,input().split())
#    h=list(map(int,input().split()))
#    p=True
#    c=0
#    for i in range(n-1):
#        if h[i+1]-h[i]<=u and h[i]<=h[i+1] or h[i]-h[i+1]<=d and h[i]>=h[i+1]:
#            None
#        elif p and h[i]>h[i+1]:  
#            p=False
#        else:
#            break
#        c+=1
#    print(c+1)