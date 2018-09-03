def d(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
for i in range(int(input())):
    r = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    if d(a,b) <= r and d(a,c) <= r or d(b,a) <= r and d(b,c) <= r or d(c,a) <= r and d(c,b) <= r:
        print('yes')
    else:
        print('no')