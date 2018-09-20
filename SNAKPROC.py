for i in range(int(input())):
    input()
    flag = False
    for i in input():
        if i == '' or i=='.':
            continue
        elif i == 'H' and not flag:
            flag = True
        elif i == 'T' and flag:
            flag = False
        elif i == 'T' and not flag:
            flag = True
            break
        else:
            break
    print('Valid' if not flag else 'Invalid' )