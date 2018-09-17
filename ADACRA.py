#for i in range(int(input())):
#    n = input()
#    flag = n[0]
#    c = 0
#    for i in range(1,len(n)):
#        if n[i] != flag:
#            c+=1
#            flag = n[i]
#    if c%2==0:
#        print(c//2)
#    else:
#        print((c+1)//2)
for i in range(int(input())):
    s = input()
    print(s.count('U'+'D' if s[0] == 'U' else 'D'+'U'))
