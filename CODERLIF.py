#for i in range(int(input())):
#    a = ''
#    for i in input().split():
#        if i == '1':
#            a+=i
#        elif i=='0':
#            a = ''
#        if len(a) > 5:
#            print("#coderlifematters")
#            break
#        
#    else:
#        print("#allcodersarefun")
for i in range(int(input())):
    for i in ''.join(input().split()).split('0'):
        if len(i) > 5:
            print("#coderlifematters")
            break
    else:
        print("#allcodersarefun")