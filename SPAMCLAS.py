for i in range(int(input())):
    n,minx,maxx=map(int,input().split())
    w=[]
    a=[]
    yes=no=0
    wl=False
    al=True
    for i in range(n):
        l1,l2=map(int,input().split())
        w.append(l1)
        a.append(l2)
        if l1%2==0:
            wl=True
            if l2%2==1:
                al=False
    
#    if wl and al:
#        if a[n-1]%2==0:
#            no=maxx-minx+1
#        else:
#            yes=maxx-minx+1
#    
#    else:
#        if (minx*w[0]+a[0])%2==0:
#            no=(maxx-minx+1)//2+1
#            yes=(maxx-minx+1)//2
#        
#        elif (minx*w[0]+a[0])%2==0:
#            no=(maxx-minx+1)//2
#            yes=(maxx-minx+1)//2+1
#        
#        else:# (maxx-minx+1)%2==0:
#            yes=no=(maxx-minx+1)//2
    
            
    print(no,yes)