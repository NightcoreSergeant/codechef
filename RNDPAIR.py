for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    l = []
    for i in range(n):
        for j in range(i+1, n):
            l.append(a[i]+a[j])
            print(j)
    print("{0:.8f}".format(l.count(max(l))/len(l)))
