def line(a1,a2,b1,b2):
    return (a1-b1)**2+(a2-b2)**2

c=0
for i in range(int(input())):
    x1, y1, x2, y2, x3, y3=map(int,input().split())
    x=[line(x1,y1,x2,y2),line(x3,y3,x2,y2),line(x1,y1,x3,y3)]
    x.sort()
    if x[0]+x[1]==x[2]:
        c+=1
print(c)