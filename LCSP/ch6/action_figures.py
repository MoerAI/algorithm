# https://acm.timus.ru/problem.aspx?space=1&num=2144

# 액션 피규어가 담긴 상자를 모두 선반에 놓아야 함
# 1 ~ n개의 상자를 가지고 있음
# 상자 번호 i에는 각각 고유한 크기의 aij를 가진 ki 액션 피규어가 들어 있음
# 모든 그림을 크기에 따라 증가하는 순서로 배치
# 상자를 앞뒤로 중복 배치하는 것은 불가능
# 청소가 가능한지 여부를 구하라

n = int(input())
boxes = []
    
for _ in range(n):
    data = list(map(int, input().split()))
    ki = data[0]
    sizes = data[1:]
    
    # 한 상자의 최소값과 최대값을 추출
    min_size = min(sizes)
    max_size = max(sizes)
    
    # 상자를 리스트로 추가
    boxes.append((min_size, max_size))

# 최소값을 기준으로 상자를 정렬
boxes.sort()

# 상자들을 확인하면서, 이전 상자의 최대값보다 현재 상자의 최소값이 작으면 NO
for i in range(1, n):
    if boxes[i-1][1] > boxes[i][0]:
        print("NO")

print("YES")