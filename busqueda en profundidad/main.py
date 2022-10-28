def DFS(graph):
    visited = [False for _ in graph]

    def dfs(i=0):
        graph[i] = True
        for j in range(len(graph)):
            if graph[j] == False:
                dfs(j)