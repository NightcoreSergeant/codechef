for i in range(int(input())):
    j=input()
    s=input()
    c=0
    visited=set()
    for i in j:
        if i not in visited:
            c+=s.count(i)
            visited.add(i)
    print(c)