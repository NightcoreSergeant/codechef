from math import sqrt

def distnace(a,b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
#
#def bfs(quee,l,s, r):
#    x = len(quee)
#    for i in quee:
#        for j in range(len(l)):
#            if i != l[j] and distnace(i, l[j]) <= r:
#               quee.append(l[j])
#    for i in range(x):
#        if quee[0] not in s:    
#            s.append(quee[0])
#        quee.pop(0)
#    if len(quee) == 0:
#        return len(s)
#    else:
#        bfs(quee, l, s, r)
#

def bfs(graph, start,r):
    visited, quee = set(), [start]
    while quee:
        lenquee = len(quee)
        for j in quee:
            for i in range(len(graph)):
                if distnace(j, graph[i]) <= r and graph[i] not in visited:
                    quee.append(graph[i])
        
        for i in range(lenquee):
            visited.add(quee.pop(0))            
    return len(visited)

for i in range(int(input())):
    l = []
    n, r = map(int,input().split())
    for _ in range(n):
        l.append(list(map(int,input().split())))
    quee = [l[0]]
    if bfs(l, l[0],r) == n:
        print(True)
    
    else:
        print(False)

