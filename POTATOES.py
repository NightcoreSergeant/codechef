primes=[2]
for i in range(2,2004):
    for j in primes:
        if i%j==0:
            break
    else:
        primes.append(i)
for i in range(int(input())):
    x,y=map(int,input().split())
    x+=y
    for i in primes:
        if x<i:
            print(i-x)
            break