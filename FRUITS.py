#for i in range(int(input())):
#    n,m,k = map(int,input().split())
#    print('0' if max(n,m)-min(n,m)-k < 0 else max(n,m)-min(n,m)-k)
for i in range(int(input())):
    n,m,k=map(int,input().split())
    print(max(abs(n-m)-k,0))
