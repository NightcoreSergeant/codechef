def make_a_graph(node,a,b):
    node=list(map(list,node))
    node[a[0]][a[1]],node[b[0]][b[1]]=node[b[0]][b[1]],node[a[0]][a[1]]
    node=tuple(map(tuple,node))
    return node
prime=[3,5,7,11,13,17]
y=((1,2,3),(4,5,6),(7,8,9))
queue=[y]
visited={y:0}
while queue:
    node=queue.pop()
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

#print(visited)
for i in range(int(input())):
    input()
    x=tuple(map(int,input().split()))
    y=tuple(map(int,input().split()))
    z=tuple(map(int,input().split()))
    x=(x,y,z)
    try:
        print(visited[x])
    except:
        print(-1)
        
