#x = [1, 2 ,5, 10, 50, 100]
#for _ in range(int(input())):
#    N = int(input())
#    counter = 0
#    i = len(x) - 1
#    while N != 0:
#        if x[i] <= N:
#            N -= x[i]
#            counter += 1
#        else:
#            i -= 1
#    print(counter)
#
#better one
x = [100,50,10,5,2,1]
for _ in range(int(input())):
    N = int(input())
    counter = 0
    for i in x:
        if N == 0:
            break
        counter += (N//i)
        N %= i
    print(counter)