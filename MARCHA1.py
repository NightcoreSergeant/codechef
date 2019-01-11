##brute force
#import random
#ans=['No','Yes']
#for i in range(int(input())):
#    flag=0
#    n,m=map(int,input().split())
#    l=[]
#    for i in range(n):
#        x=int(input())
#        if x<=m:
#            l.append(x)
#        if x==m:
#            flag=1
#    t=10000
#    c=0
#    visited=set()
#    while flag!=1 and t!=0:
#        x=random.randrange(0,len(l))
#        if x not in visited:
#            c+=l[x]
#            visited.add(x)
#        if c>m:
#            c=0
#            visited=set()
#        if c==m:
#            flag=1
#        t-=1
#    print(ans[flag])
##kind of bfs...very slow, bruteforce is faster
#for i in range(int(input())):
#    l=[]
#    n,m=map(int,input().split())
#    for i in range(n):
#        x=int(input())
#        if x<m:
#            l.append(x)
#    quee=[l]
#    visited=[]
#    flag=False
#    while quee:
#        node=quee.pop(0)
#        visited.append(node)
#        for i in range(len(node)-1):
#            for j in range(i+1,len(node)):
#                x=[i for i in node]
#                x[i]=x[i]+x[j]
#                x.pop(j)
#                if x not in visited:
#                    quee.append(x)
#                
#                if m in x:
#                    flag=True
#                    break
#            if flag:
#                break
#        if flag:
#            break
#    if flag:
#        print('Yes')
#    else:
#        print('No')
#
def comb(l,i,m):
    if m==0:return True
    if i==len(l):return False
    if m<0:return False
    return comb(l,i+1,m) or comb(l,i+1,m-l[i])

for i in range(int(input())):
    flag=False
    n,m=map(int,input().split())
    l=[]
    for i in range(n):
        x=int(input())
        if x<m:
            l.append(x)
        if x==m:
            flag=True
    if flag==False:
        flag=comb(l,0,m)
    print(['No','Yes'][flag])
    
