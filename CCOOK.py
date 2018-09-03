for i in range(int(input())):
    x = sum(list(map(int,input().split())))
    if x == 0:
        print("Beginner")
    elif x == 1:
        print("Junior Developer")
    elif x == 2:
        print("Middle Developer")
    elif x == 3:
        print("Senior Developer")
    elif x == 4:
        print("Hacker")
    else:
        print("Jeff Dean")