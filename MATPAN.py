a = 'abcdefghijklmnopqrstuvwxyz'
for i in range(int(input())):
    st = list(map(int,input().split()))
    n = input()
    c = 0
    for i in range(0,26):
        if a[i] not in n:
            c+=st[i]
    print(c)
