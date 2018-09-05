for i in range(int(input())):
    n = input()
    if n.count('3') >= 3:
        n= str(int(n) + 1)
    while n.count('3') < 3:
        n= str(int(n) + 1)
    print(n)
