#from collections import deque
def make_a_graph(node,a,b):
    node=list(map(list,node))
    node[a[0]][a[1]],node[b[0]][b[1]]=node[b[0]][b[1]],node[a[0]][a[1]]
    node=tuple(map(tuple,node))
    return node

prime={3,5,7,11,13,17}
y=((1,2,3),(4,5,6),(7,8,9))
queue=[y]
visited={y:0}

while queue:
    node=queue.pop(0)
    for i in range(2):
        for j in range(3):
            if node[i][j]+node[i+1][j] in prime:
                z=make_a_graph(node,[i,j],[i+1,j])
                if z not in visited:    
                    queue.append(z)
                    visited[z]=visited[node]+1
    for i in range(3):
        for j in range(2):
            if node[i][j]+node[i][j+1] in prime:
                z=make_a_graph(node,[i,j],[i,j+1])
                if z not in visited:
                    queue.append(z)
                    visited[z]=visited[node]+1

for i in range(int(input())):
    input()
    x=tuple(map(int,input().split()))
    y=tuple(map(int,input().split()))
    z=tuple(map(int,input().split()))
    x=(x,y,z)
    if x in visited:
        print(visited[x])
    else:
        print(-1)
        
from collections import deque
def graph(node,a,b):
    node=list(node)
    node[a],node[b]=node[b],node[a]
    node=tuple(node)
    return node
prime={3,5,7,11,13,17}
y=(1,2,3,4,5,6,7,8,9)
queue=deque()
queue.append(y)
visited={y:0}
while queue:
    node=queue.popleft()
    for i in range(3):
        if node[i+3]+node[i+6] in prime:
            x=graph(node,i+3,i+6)
            if x not in visited:
                queue.append(x)
                visited[x]=visited[node]+1
        if node[i]+node[i+3] in prime:
            x=graph(node,i,i+3) 
            if x not in visited:
                queue.append(x)
                visited[x]=visited[node]+1
        if i!=2:
            if node[i]+node[i+1] in prime:
                x=graph(node,i,i+1)
                if x not in visited:
                    queue.append(x)
                    visited[x]=visited[node]+1
            if node[i+3]+node[i+4] in prime:
                x=graph(node,i+3,i+4)
                if x not in visited:
                    queue.append(x)
                    visited[x]=visited[node]+1
            if node[i+6]+node[i+7] in prime:
                x=graph(node,i+6,i+7) 
                if x not in visited:
                    queue.append(x)
                    visited[x]=visited[node]+1
for i in range(int(input())):
    input()
    x=tuple(map(int,(input()+input()+input()).split()))
    if x in visited:
        print(visited[x])
    else:
        print(-1)
