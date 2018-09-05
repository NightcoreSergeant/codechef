for i in range(int(input())):
    n = int(input())
    x = input()
    print(n-max(x.count('G'),x.count('B'),x.count('R')))
