for i in range(int(input())):
    a = input()
    b = input()
    print(''.join('W' if i == 'B' and j == 'B' else 'B' for i, j in zip(a,b)))
