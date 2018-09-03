for _ in range(int(input())):
    x = 0
    D, N = map(int,input().split())
    N += 1
    for i in range(D):
        for i in range(N):
            x += i
        N = x
    print(N)