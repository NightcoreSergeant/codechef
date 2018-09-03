for i in range(int(input())):
    k, l = map(int,input().split())
    n = list(input().split())
    arr = ""
    ans = []
    for i in range(l):
        arr += input()
    for i in n:
        if i in arr:
            ans.append("YES")
        else:
            ans.append("NO")
    print(" ".join(ans))