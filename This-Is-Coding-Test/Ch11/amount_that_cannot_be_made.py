import pytest


@pytest.mark.parametrize(
    'n, data, expected',
    [(5, [3, 2, 1, 1, 9], 8),
     (3, [3, 5, 7], 1),
     (4, [1, 2, 3, 8], 7),
     (4, [1, 2, 2, 8], 6)]
)
def test_solve(n, data, expected):
    result = solve(n, data)
    assert result == expected


def solve(n, data):
    data.sort()

    target = 1
    for x in data:
        if target < x:
            break
        target += x

    return target