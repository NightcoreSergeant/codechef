for i in range(int(input())):
    c=s=a=b=0
    for i in input():
        if i == 'A' and s==1:
            a+=1
            a+=c
            c=0
        elif i == 'A':
            c=0
            a+=1
            s=1
        elif i == 'B' and s==-1:
            b+=1
            b+=c
            c=0           
        elif i == 'B':
            b+=1
            s=-1
            c=0
        elif s!=0:
            c+=1
    print(a,b)