for i in range(int(input())):
    input()
    v = list(map(int,input().split()))
    v.sort()
    ost = 10**6
    for i in range(len(v)):
        if abs(v[i] - v[i-1]) < ost:
            ost = abs(v[i] - v[i-1])
        elif ost == 0:
            print(0)
            break
    else:
        print(ost)

