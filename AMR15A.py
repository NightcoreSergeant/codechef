n = int(input())
a = list(map(int,input().split()))
counter = 0
for i in range(n):
    if a[i] % 2 == 0:
        counter += 1
if counter > n//2:
    print("READY FOR BATTLE")
else:
    print("NOT READY")