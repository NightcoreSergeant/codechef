def spamclas(N, minx, maxx):
    neurons = []
    a = 1
    al = 0
    for i in range(N):
        neurons.append(list(map(int, input().split())))
        if neurons[i][0] % 2 == 0:
            a = 0
    if a == 0:
        for i in range(N):
            al += neurons[i][1]
        if al % 2 == 0:
            return '{} 0'.format(maxx - minx+1)
        else:
            return '0 {}'.format(maxx - minx+1)
    
    else:
        if (maxx - minx + 1) % 2 == 0:
            return '{} {}'.format((maxx - minx+1) //2, (maxx - minx+1) //2)
        
        if (minx * neurons[0][0] + neurons[0][1]) % 2 == 0:
            return '{} {}'.format((maxx - minx + 1) //2 + 1, (maxx - minx + 1) //2)
        
        else:
            return '{} {}'.format((maxx - minx + 1) //2, (maxx - minx+1) //2 + 1)




#spamer               return '{} {}'.format((maxx - minx + 1) //2, (maxx - minx+1) //2 + 1)
#nonspamer            return '{} {}'.format((maxx - minx + 1) //2 + 1, (maxx - minx + 1) //2)



for i in range(int(input())):
    N, minx, maxx = map(int, input().split())
    print(spamclas(N, minx, maxx))
