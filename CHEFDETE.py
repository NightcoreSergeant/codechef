n=int(input())
r=set(input().split())
ans=[]
for i in range(1,n+1):
    if str(i) not in r:
        ans.append(str(i))
print(' '.join(ans))