INF = int(1e9)

n, m = map(int, input().split())
graph =  [[INF] * (n + 1) for _ in range(n + 1)]

# 그래프 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받음
for _ in range(1, n + 1):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 플로이드 워셜 알고리즘
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 학생들 한 명 한 명 확인하면서 체크
result = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1
print(result)