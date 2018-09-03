for i in range(int(input())):
    input()
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.remove(max(a))
    b.remove(max(b))
    a = sum(a)
    b = sum(b)
    if a > b:
        print("Bob")
    elif a < b:
        print("Alice")
    else:
        print("Draw")