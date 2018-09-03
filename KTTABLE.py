for i in range(int(input())):
    x = int(input())
    a = [0] + list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = 0
    for i in range(x):
        if a[i+1] - a[i] >= b[i]:
            c += 1
    print(c)