from collections import defaultdict
def solution(n, res):
    graph = defaultdict(list)
    for v1, v2 in res:
        graph[v1].append(v2)
    print(graph)
    visited = [False] * (n + 1)
    while n >= 1:
        start = n - 1
        dfs(graph, n, visited)
        print(n, end = ' ')
        n -= 1
            
def dfs(graph, v, visited):
    visited[v] = True
    for li in graph[v]:
        
print(solution(5,[[3,2],[3,0],[4,3],[1,4]]))