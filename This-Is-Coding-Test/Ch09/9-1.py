import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

print("노드의 개수, 간선의 개수를 입력해 주세요.")
n, m = map(int, input().split())
print("시작 노드 번호를 입력해 주세요.")
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]
