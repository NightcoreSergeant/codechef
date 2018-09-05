for i in range(int(input())):
    input()
    l = list(map(int,input().split()))
    r = list(map(int,input().split()))
    lr = 0
    mr = 0
    index = 0
    for i in range(len(l)):
        if lr < l[i]*r[i]:
            lr = l[i]*r[i]
            index = i
            mr = r[i]
        elif lr == l[i]*r[i] and mr < r[i]:
            index = i 
            mr = r[i]
            lr = l[i]*r[i]
    print(index+1)
