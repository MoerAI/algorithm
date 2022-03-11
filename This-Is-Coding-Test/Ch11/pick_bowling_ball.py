import pytest


@pytest.mark.parametrize(
    'n, m, data, expected',
    [(5, 3,
      [1, 3, 2, 3, 2],
      8),
     (8, 5,
      [1, 5, 4, 3, 2, 4, 5, 2],
      25)]
)
def test(n, m, data, expected):
    result = solution(n, m, data)
    assert result == expected

def solution(n, m, data):
    array = [0] * 11

    for x in data:
        array[x] += 1

    result = 0

    for i in range(1, m + 1):
        n -= array[i]
        result += array[i] * n
    print(result)