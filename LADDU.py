for i in range(int(input())):
    act,indian = input().split()
    c = 0
    for i in range(int(act)):
        a = input().split()
        if len(a) == 1:
            a.append(0)
        if a[0] == 'CONTEST_WON' and int(a[1]) > 20:
            c += 300
        elif a[0] == 'CONTEST_WON':
            c+= 300-int(a[1])+20
        elif a[0] == 'TOP_CONTRIBUTOR':
            c+=300
        elif a[0] == 'BUG_FOUND':
            c+=int(a[1])
        elif a[0] == 'CONTEST_HOSTED':
            c+=50
    print(c//200 if indian == 'INDIAN' else c//400)
