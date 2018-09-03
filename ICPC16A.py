for i in range(int(input())):
    x = list(map(int,input().split()))
    if x[0] != x[2] and x[1] != x[3]:
        print('sad')
    elif x[0] < x[2]:
        print('right')
    elif x[1] < x[3]:
        print('up')
    elif x[0] > x[2]:
        print('left')
    else:
        print('down')