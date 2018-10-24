for i in range(int(input())):
    input()
    c=1
    ans=['1']
    a = list(map(int,input().split()))
    for i in range(len(a)-2,-1,-1):
        if a[i]<0 and a[i+1]>0 or a[i]>0 and a[i+1]<0:
            c+=1
        else:
            c=1
        ans.append(str(c))
    print(' '.join(ans[::-1]))