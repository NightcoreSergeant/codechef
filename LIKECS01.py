for i in range(int(input())):
    s = input()
    flag = False
    for i in range(len(s)-3):
        for j in range(i+1,len(s)-2):
            x = s[j+1:]
            print(x)
            if s[i] in x and s[j] in x:
                pi = []
                pj = []
                for c in range(len(x)):
                    if s[c] == s[j]:
                        pj.append(c)
                    if s[c] == s[i]:
                        pi.append(c)
                if min(pi) < max(pj):
                    print('yes')
                    flag = True
                    break
        if flag:
            break
    else:
        print('no')
