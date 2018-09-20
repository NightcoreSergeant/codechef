for i in range(int(input())):
    a,b = input(),input()
    for i in a:
        if i in b:
            print('Yes')
            break
    else:
        print('No')
