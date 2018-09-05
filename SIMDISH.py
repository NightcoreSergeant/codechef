for i in range(int(input())):
    x = input().split()
    c = 0
    for i in input().split():
        if i in x:
            c+=1
    if c >= len(x)//2:
        print('similar')
    else:
        print('dissimilar')
