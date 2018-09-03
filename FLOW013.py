for i in range(int(input())):
    if sum(list(map(int,input().split()))) == 180:
        print("YES")
    else:
        print("NO")