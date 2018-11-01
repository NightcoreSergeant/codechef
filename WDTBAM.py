for i in range(int(input())):
    input()
    a = input()
    b = input()
    l = list(map(int,input().split()))
    c=0
    for i in range(len(a)):
        if a[i]==b[i]:
            c+=1
    if c==len(a):
        print(l[c])
    else:
        print(max(l[:c+1]))
