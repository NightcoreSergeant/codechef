for i in range(int(input())):
    n = int(input())
    graph = list(map(int,input().split()))+[0]
    for i in range(n-1):
        l = list(map(int,input().split()))+[0]
        for i in range(len(l)-1):
            if i == 0 or graph[i] > graph[i-1]:
                l[i] += graph[i]
            else:
                l[i] =graph[i-1]+l[i]
        graph = l
    print(max(graph))
