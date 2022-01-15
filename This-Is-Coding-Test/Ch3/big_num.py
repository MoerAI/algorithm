import pytest

# 배열의 크기 N
# 주어진 수를 M번 더하여 가장 큰 수
# 연속해서 K번 초과 불가
# 배열 array

@pytest.mark.parameterize("n,m,k,data,expected", [(5, 8, 3, [2, 4, 5, 4, 6], 46)])
def test_solve(n, m, k, data, expected):
    result = solve_m(n, m, k, data)
    assert result == expected


# 내 풀이
def solve_m(n, m, k, data):
    data.sort()
    answer = 0
    first = data[n - 1]
    second = data[n - 2]
    answer = first * k * (m//k) + second * (m % k)
    return answer
# 가장 큰 값과 두번째로 큰 값 찾기
# first = second = -float('inf') #최소값으로 설정
# for e in data:
#     if e > first:
#         second = first
#         first = e
#     elif second < e < first:
#         second = e


# 교재 풀이 1
def solve1(n, m, k, data):
    data.sort()
    first = data[n - 1]
    second = data[n - 2]
    answer = 0
    count = m
    while True:
        for i in range(k):
            if count == 0:
                break
            answer += first
            count -= 1

        if count == 0:
            break
        answer += second
        count -= 1
    return answer


# 교재 풀이 2
def solve2(n, m, k, data):
    data.sort()
    first = data[n - 1]
    second = data[n - 2]
    answer = 0
    count = m

    count = int(m / (k + 1)) * k
    count += m % (k + 1)

    answer = 0
    answer += (count) * first
    answer += (m - count) * second

    return answer