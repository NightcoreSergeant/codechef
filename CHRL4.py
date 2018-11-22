n,k=map(int,input().split())
l=list(map(int,input().split()))

if n==1:
    print(l[0])
elif k>=n:
    print(l[0]*l[n-1])
else:
    