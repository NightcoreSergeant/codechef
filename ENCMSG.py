a ='abcdefghijklmnopqrstuvwxyz'
for i in range(int(input())):
    input()
    s = input()
    b = []
    for i in range(0,len(s)-1,2):
        b.append(s[i+1]+s[i])
    if len(s)%2==1:
        b.append(s[-1])
    s = ''.join(b)
    b = []
    for i in s:
        b.append(a[-1-a.find(i)])
    print(''.join(b))
