for _ in range(int(input())):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))
    counter = 0
    for i in arr:
        if (i + K)% 7 == 0:
            counter += 1
    print(counter)