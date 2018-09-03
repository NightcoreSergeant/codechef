def stones(a,b,c,x,y):
    if a + b + c != x + y or min(a,b,c) > min(x,y):
        return 'NO'
    else:
        return 'YES'


for i in range(int(input())):
    a,b,c,x,y = map(int, input().split())
    print(stones(a,b,c,x,y))

