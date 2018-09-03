for _ in range(int(input())):
    i, ii, iii = map(float,input().split())
    if i > 50 and ii < 0.7 and iii > 5600:
        print(10)
    elif i > 50 and ii < 0.7:
        print(9)
    elif ii < 0.7 and iii > 5600:
        print(8)
    elif i > 50 and iii > 5600:
        print(7)
    elif i > 50 or ii < 0.7 or iii > 5600:
        print(6)
    else:
        print(5)