for i in range(int(input())):
    n, k = map(int,input().split())
    print(sorted(list(map(int,input().split())))[((n+k)//2)])