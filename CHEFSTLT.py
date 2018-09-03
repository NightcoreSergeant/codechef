for _ in range(int(input())):
    s1, s2 = input(), input()
    maxi = mini = 0
    for i in range(len(s1)):
        if s1[i] != s2[i] or s1[i] == '?' or s2[i] == '?':
            maxi += 1
        if s1[i] != s2[i] and s1[i] != '?' and s2[i] != '?':
            mini += 1
    print(mini,maxi)
