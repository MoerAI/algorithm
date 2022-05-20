import pytest
from collections import deque

@pytest.mark.parametrize(
    'n, m, k, x, array, expected',
    [(4, 4, 2, 1,
      [(1, 2), (1, 3), (2, 3), (2, 4)],
      "4"),
     (4, 3, 2, 1,
      [(1, 2), (1, 3), (1, 4)],
      "-1"),
     (4, 4, 1, 1,
      [(1, 2), (1, 3), (2, 3), (2, 4)],
      "2\n3"),
     ]
)
def test(n, m, k, x, array, expected):
    result = solution(n, m, k, x, array)
    assert result == expected
 
def solution(n, m, k, x, array):
    # 모든 도시에 대한 최단 거리 초기화
    distance = [-1] * (n + 1)
    distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정
    
    # 너비 우선 탐색 BFS 수행
    q = deque([x])
    while q:
        now = q.popleft()
        # 현재 도시에서 이동할 수 있는 모든 도시를 확인
        for next_node in array[now]:
            # 아직 방문하지 않은 도시라면
            if distance[next_node] == -1:
                # 최단 거리 갱신
                distance[next_node] = distance[now] + 1
                q.append(next_node)
    # 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
    result = ""
    for i in range(1, n + 1):
        if distance[i] == k:
            result += str(i) + '\n'
        return result
    # 만약 최단 거리가 K인 도시가 없다면, -1 출력
    if result == '':
        return "-1"