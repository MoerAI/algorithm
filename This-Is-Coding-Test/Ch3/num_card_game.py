# N(행), M(열) 크기의 배열 입력 받기
n, m = map(int, input().split())

answer = 0
low_value = []

for i in range(n):
    data = list(map(int, input().split()))
    low_value.append(min(data))
    answer = max(low_value)

print(answer)

# 교재 풀이1
answer = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수' 중에서 가장 큰 수 찾기
    answer = max(answer, min_value) # 자연수 조건 때문에 이렇게 가능하네

print(answer)

# 교재 풀이2
answer = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 1001
    for a in data:
        min_value = min(min_value, a)
    answer = max(answer, min_value)

print(answer)