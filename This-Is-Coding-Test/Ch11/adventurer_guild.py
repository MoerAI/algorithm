import pytest

@pytest.mark.parametrize(
    "n, data, expected",
    [(5,
      [2, 3, 1, 2, 2],
      2),
     (3,
      [1, 1, 1],
      3),
     (4,
      [1, 1, 1, 2],
      3),
     (5,
      [4, 1, 1, 1, 1],
      4)
     ]
)
def test_solve(n, data, expected):
    result = solve(n, data)
    assert result == expected


def solve(n, data):
    count = 0
    result = 0
    data.sort()

    for i in data:
        count += 1
        if count >= i:
            result += 1
            count = 0

    return result