def a(a):
    for i in range(2, a//2):
        if a%i == 0:
            return "no"
    return "yes"

for i in range(int(input())):
    print(a(int(input())))
