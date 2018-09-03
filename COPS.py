#for _ in range(int(input())):
#    m,x,y= map(int,input().split())
#    arr = list(map(int,input().split()))
#    z = set()
#    for i in arr:
#        for j in range(i, i+(x*y)+1):
#            if j < 101:
#                z.add(j)
#        for j in range(i, i-(x*y)-1, -1):
#            if j > 0:
#                z.add(j)
#            
#    print(100-len(z))
for _ in range(int(input())):
    m,x,y = map(int,input().split())
    arr = list(map(int,input().split()))
    z = 0
    arr.sort()
    for i in range(len(arr)):
        if i == 0:
            z+=max(arr[i]-x*y-1, 0)
        
        else:
            z+=max(arr[i]-arr[i-1]- 2*x*y -1, 0)
        
        if i == len(arr)-1:
            z+=max(100-arr[i]-x*y, 0)
    print(z)