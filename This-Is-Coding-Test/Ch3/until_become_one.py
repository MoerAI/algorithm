import pytest
# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
# 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.

@pytest.mark.parametrize("n,k,expected", [(25, 5, 2), (107, 3, 10)])
def test_solve(n, k, expected):
    count = solve_m(n, k)
    assert count == expected


# 나의 풀이
def solve_m(n, k):
    n, k = map(int, input().split())
    answer = 0

    # n이 1이 될 때까지
    while n != 1:
        # n을 k로 나눌 수 있으면 나누고 그렇지 않으면 1씩 빼기
        n = n / k if n % k == 0 else n - 1
        answer += 1

    return answer


# 교제 풀이 1
def solve1(n, k):
    result = 0
    # N이 K이상이라면 K로 계속 나누기
    while n >= k:
        # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
        while n % k != 0:
            n -= 1
            result += 1
        # K로 나누기
        n //= k
        result += 1

        # 마지막으로 남은 수에 대하여 1씩 빼기
        while n > 1:
            n -= 1
            result += 1

    return result


# 교제 풀이02
def solve2(n, k):
    result = 0

    while True:
        # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
        target = (n // k) * k
        result += (n - target)
        n = target
        # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
        if n < k:
            break
        # K로 나누기
        result += 1
        n //= k

    result += (n - 1)

    return result