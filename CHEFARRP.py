for _ in range(int(input())):
    N = int(input())
    arr = list(map(int,input().split()))
    counter = 0
    for i in range(N):
        sumx = 0
        multiply = 1
        for j in range(i, N):
            sumx += arr[j]
            multiply *= arr[j]
            
            if sumx == multiply:
                counter += 1

    print(counter)