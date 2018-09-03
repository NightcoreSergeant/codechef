#for i in range(int(input())):
#    x = int(input())
#    c = 0
#    y = 0
#    for i in range(1, x+1//2):
#        y+=i
#        if y <= x:
#            c+=1
#        else:
#            break
#    print(c)

#best
for i in range(int(input())):
    x = int(input())
    d = 1+8*x
    x1 = ((d ** 0.5)-1)//2
    print(int(x1))