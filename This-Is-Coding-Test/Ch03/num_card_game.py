import pytest
# 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드를 한 장 뽑는 게임
# 1. 숫자가 쓰인 카드들이 N x M 형태로 놓여 있다. 이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
# 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
# 3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
# 4. 따라서 처음에 카드를 골라낼 행을 선택할 때,
# 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
# 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

@pytest.mark.parametrize(
    "n,m,data,expected",
    [(2, 4, [7, 3, 1, 8, 3, 3, 3, 4], 3),
     (3, 3, [3, 1, 2, 4, 1, 4, 2, 2, 2], 2)]
)
def test_solve(n, m, data, expected):
    num = solve_m(n, m, data)
    assert num == expected


#나의 풀이
def solve_m(n, m, data):
    answer = 0
    low_value = []

    for i in range(n):
        data = list(map(int, input().split()))
        low_value.append(min(data))
        answer = max(low_value)

    return answer


# 교재 풀이1
def solve1(n, m, data):
    answer = 0
    # 한 줄씩 입력받아 확인
    for i in range(n):
        data = list(map(int, input().split()))
        # 현재 줄에서 '가장 작은 수' 찾기
        min_value = min(data)
        # '가장 작은 수' 중에서 가장 큰 수 찾기
        answer = max(answer, min_value) # 자연수 조건 때문에 이렇게 가능하네

    return answer


# 교재 풀이2
def solve2(n, m, data):
    answer = 0
    for i in range(n):
        data = list(map(int, input().split()))
        min_value = 1001
        for a in data:
            min_value = min(min_value, a)
        answer = max(answer, min_value)

    return answer