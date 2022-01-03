# 큰 수의 법칙
# 배열의 크기 N, 더하기 횟수 M, 한개 원소 여러번 더하기 최댓값 K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))
#데이터 정렬
data.sort()
first = data[n - 1]
second = data[n - 2]
answer = first * k * (m//k) + second * (m % k)
print(answer)

# 시도하다가 만든 가장 큰 값과 두번째로 큰 값 찾기
# first = second = -float('inf') #최소값으로 설정
# for e in data:
#     if e > first:
#         second = first
#         first = e
#     elif second < e < first:
#         second = e

# 교재 풀이 1
answer = 0
count = m
while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if count == 0:
            break
        answer += first
        count -= 1 # 더할 때마다 1씩 빼기

    if count == 0: # m이 0이라면 반복문 탈출
        break
    answer += second # 두 번째로 큰 수를 한 번 더하기
    count -= 1 # 더할 때마다 1씩 빼기

print(answer) # 최종 답안 출력

# 교재 풀이 2
count = int(m / (k + 1)) * k
count += m % (k + 1)

answer = 0
answer += (count) * first # 가장 큰 수 더하기
answer += (m - count) * second # 두 번째로 큰 수 더하기

print(answer)