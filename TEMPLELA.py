for i in range(int(input())):
    input()
    a = list(map(int,input().split()))
    if len(a)%2==1 and a == a[::-1] and a[0] == 1:
        for i in range(len(a)//2):
            if a[i+1]-a[i] != 1:
                print('no')
                break
        else:
            print('yes')
    else:
        print('no')

