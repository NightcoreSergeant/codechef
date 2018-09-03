for _ in range(int(input())):
    x = 0
    for i in range(int(input()), 0, -2):
        x += i**2
    print(x)