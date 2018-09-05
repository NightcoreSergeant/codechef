for i in range(int(input())):
    x1,x2,x3,v1,v2 = map(int,input().split())
    a = abs(x1-x3)/v1
    b = abs(x2-x3)/v2
    if a < b:
        print('Chef')
    elif a > b:
        print('Kefa')
    else:
        print('Draw')

