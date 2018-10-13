for i in range(int(input())):
    a=2
    for i in input():
        if i=='C' and a==2:
            continue
        elif i=='E' and a>=1:
            a=1
        elif i=='S' and a>=0:
            a=0
        else:
            print('no')
            break
    else:
        print('yes')
