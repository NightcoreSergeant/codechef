for i in range(int(input())):
    input()
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    print(min(sum(x[::2]+y[1::2]),sum(x[1::2]+y[::2])))
