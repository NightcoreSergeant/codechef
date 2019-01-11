##algorythm for all primes between two numbers to 10**9
#import math
#
#primes=[0,0,True]+[True,False]*(31622//2)
#p=[]
#flag=False
#for i in range(3,31622,2):
#    if primes[i]:
#        x=i**2
#        if x>31622:
#            break
#        for j in range(x,31622+1,2*i):
#            primes[j]=False
#    
#    if flag:
#        break
#
#for i in range(len(primes)):
#    if primes[i]:
#        p.append(i)
#
#for j in range(int(input())):
#    m,n=map(int,input().split())
#    if m==1 and n!=1:
#        m+=1
#    for i in range(m,n+1):
#        x=int(math.sqrt(i))
#        for j in p:
#            if x<j:
#                print(i)
#                break
#            if i%j==0:
#                break
#        else:
#            print(i)
#    print('')
##better solution
def segpr(m,n, basepr):
    seg=[True]*(n-m+1)
    if m==1:seg[0] = False
    ls=len(seg)
    for p in basepr:
        if m>p:
            st=p-m%p
            if st==p:
                st=0
        else:
            st=2*p-m
        for ix in range(st, ls, p):
            seg[ix] = False
    return tuple(m+ix for ix in range(ls) if seg[ix])

lim = 31623 # approx sqrt(10**9)
ispr = [0,0,True] + [True,False]*(lim//2)
basepr = [2]
for c in range(3,lim,2):
    if ispr[c]:
        csq = c*c
        if csq>lim: break
        for m in range(csq,lim+1,2*c):
            ispr[m] = False
basepr.extend(c for c in range(3,lim+1,2) if ispr[c])

for _ in range(int(input())):
    m,n = map(int,input().split())

    poss = segpr(m,n,basepr)
    if len(poss)>0:
        print('\n'.join(map(str,poss)))
    print('')
