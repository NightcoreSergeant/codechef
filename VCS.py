for _ in range(int(input())):
    n, m, k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c1 = 0
    c2 = 0
    for i in range(1, n+1):
        if i in a and i in b:
            c1 += 1
        if i not in a and i not in b:
            c2 += 1
    print(c1, c2)