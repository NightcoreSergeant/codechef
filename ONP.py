for i in range(int(input())):
    ans = ''
    signs = []
    for i in input():
        if 'z' >= i >= 'a':
            ans+=i
        elif i == '(':
            pass
        elif i == ')':
            ans += signs.pop()
        else:
            signs.append(i)
    print(ans)

