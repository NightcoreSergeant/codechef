x,y=map(int,input().split())
x=str(x-y)
if int(x[len(x)-1])>1:
    print(int(x)-1)
else:
    print(int(x)+1)
