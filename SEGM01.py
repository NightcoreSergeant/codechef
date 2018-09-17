#for i in range(int(input())):
#    flag = True
#    c = 0
#    for i in input():
#        if i == '1' and flag:
#            c+=1
#            flag = False
#        elif i == '0':
#            flag = True
#        if c>1:
#            break
#    if c == 1:
#        print("YES")
#    else:
#        print("NO")
#for i in range(int(input())):
#    a = input()
#    b = a.find('1')
#    x = len(a) - a[::-1].find('1')
#    for i in range(b,x):
#        if a[i] == '1':
#            continue
#        else:
#            print('NO')
#            break
#    else:
#        print('YES')
for i in range(int(input())):
#    y = lambda x: x.count('')
#    a = list(input().split('0'))
#    print('YES' if len(a)-y(a) == 1 else 'NO')
    print('YES' if len(list(filter(lambda x: x, input().split('0')))) == 1 else 'NO')