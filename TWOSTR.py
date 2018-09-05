for i in range(int(input())):
        flag = True
        x = input()
        y = input()
        for i in range(len(x)):
            if x[i] == '?' or y[i] == '?' or x[i] == y[i]:
                continue
            else:
                print('No')
                flag = False
                break
        if flag:
            print('Yes')   
