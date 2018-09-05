#TIME 0.50
#for i in range(int(input())):
#    n = int(input())
#    l = list(map(int,input().split()))
#    g = list(map(int,input().split()))
#    firstloop = True
#    secondloop = True
#    for i in range(n):
#        if l[i] > g[i]:
#            firstloop = False
#        if l[i] > g[-1-i]:
#            secondloop = False
#        if not firstloop and not secondloop:
#            break
#    if firstloop and not secondloop:
#        print('front')
#    elif not firstloop and secondloop:
#        print('back')
#    elif firstloop and secondloop:
#        print('both')
#    else:
#        print('none')
#TIME 0.41
for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    g = list(map(int,input().split()))
    firstloop = True
    secondloop = True
    for i in range(n):
        if l[i] > g[i]:
            firstloop = False
            break
    for i in range(n):
        if l[i] > g[-1-i]:
            secondloop = False
            break
    if firstloop and not secondloop:
        print('front')
    elif not firstloop and secondloop:
        print('back')
    elif firstloop and secondloop:
        print('both')
    else:
        print('none')
