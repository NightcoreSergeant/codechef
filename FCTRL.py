for i in range(int(input())):
    x=int(input())
    counter=0
    devider=5
    while devider<=x:
        counter+=x//devider
        devider*=5
    print(counter)