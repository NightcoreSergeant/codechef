for i in range(int(input())):
    input()
    l=sorted(list(map(int,input().split())))
    d=1000000000
    for i in range(0,len(l)-1):
        if d>abs(l[i]-l[i+1]):
            d=abs(l[i]-l[i+1])
    print(d)