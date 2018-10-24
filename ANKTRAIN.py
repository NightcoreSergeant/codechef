a = ['LB','MB','UB','LB','MB','UB','SU','SL']
for i in range(int(input())):
    n = int(input())
    c = 0
    if n%8==1 or n%8==2 or n%8==3 :
        c=n+3 
    elif n%8==4 or n%8==5 or n%8==6:
        c=n-3
    elif n%8==7:
        c=n+1
    else:
        c=n-1
    print(str(c)+a[(n%8)-1])