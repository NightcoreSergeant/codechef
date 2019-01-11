for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c1=0
    c2=0
    for i in range(n-1):
        for j in range(i+1,n):
            if a[j]<a[i] and i<j