for i in range(int(input())):
    x = input()
    c = 0
    for i in range(1,8):
        if x[i] != x[i-1]:
            c+=1
    if c <= 2:
        print('uniform')
    else:
        print('non-uniform')
