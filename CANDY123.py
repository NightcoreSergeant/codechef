for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(1,max(a,b)+2):
        if i % 2 == 1:
            a -= i
        elif i % 2 == 0:
            b -= i
        if a < 0:
            print('Bob')
            break
        elif b < 0:
            print('Limak')
            break