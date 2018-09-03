for i in range(int(input())):
    x = input()
    if x == x[::-1]:
        print("wins")
    else:
        print("losses")