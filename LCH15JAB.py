for i in range(int(input())):
    s = input()
    ls = len(s)
    l = 0
    if ls % 2 == 1:
        print("NO")
        continue
    for i in s:
        if s.count(i) == ls/2:
            print("YES")
            l = 1
            break
    if l == 0:
        print("NO")

#for _ in range(int(input())):
#    s=input()
#    s1=list(set(s))
#    l=sorted([s.count(i) for i in s1])
#    if(sum(l)-max(l)==max(l)):
#        print("YES")
#    else:
#        print("NO")