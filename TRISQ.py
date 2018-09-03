def mymethod():
    for i in range(int(input())):
        x = int(input())
        a = 0
        b = 0
        for i in range(x):
            if i % 2 == 1 and i != 0:
                a += b
                b += 1
        print(a)


for _ in range(int(input())):
    x = int(input())
    print((x//2 -1) * (x//2) //2)