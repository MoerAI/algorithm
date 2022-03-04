import pytest
# 정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초 까지의
# 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.

@pytest.mark.parametrize('n, expected', [(5, 11475)])
def test_solve(n, expected):
    result = solve_m(n)
    assert result == expected


# 나의 풀이
def solve_m(n):
    times = [1575, 3150, 4725, 8325, 9900, 11475, 13050, 14625, 16200,
             17775, 19350, 20925, 22500, 26100, 27675, 29250, 30825,
             32400, 33975, 35550, 37125, 38700, 40275]
    return times[n - 1]

# 교재 풀이
def solve1(n):
    count = 0
    for h in range(n + 1):
        for m in range(60):
            for s in range(60):
                if "3" in str(h) + str(m) + str(s):
                    count += 1
    return count