for i in range(int(input())):
    n=int(input())
    s=input()
    c=0
    x=s.count('1')
    while x!=0:
        c+=x
        x-=1
    print(c)