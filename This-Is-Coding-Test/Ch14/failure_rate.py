from cgitb import reset
import pytest
@pytest.mark.parametrize(
    'n, stages, expected',
    [5, [2, 1, 2, 6, 2, 4, 3, 3], [3, 4, 2, 1, 5]]
)
def test(n, stages, expected):
    result = solution(n, stages)
    assert result == expected

def solution(n, stages):
    stages.sort()
    people = len(stages)
    rate = []
    rank = []
    for i in range(1, n + 1):
        count = 0
        for s in stages:
            if i == s:
                count += 1
        rate.append(count/people)
        people -= count
    for i in range(1, n + 1):
        a = rate.index(max(rate))
        rank.append(a + 1)
        rate[a] = -1.0

    return rank