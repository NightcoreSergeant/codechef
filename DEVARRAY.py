n,q = map(int,input().split())
a = list(map(int,input().split()))
mina=min(a)
maxa=max(a)
for i in range(q):
    if mina <= int(input()) <= maxa:
        print('Yes')
    else:
        print('No')
