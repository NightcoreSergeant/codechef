for i in range(int(input())):
    n,v1,v2 = map(int,input().split())
    if (n*2)/v2 >= ((2**0.5)*n)/v1:
        print('Stairs')
    else:
        print('Elevator')
