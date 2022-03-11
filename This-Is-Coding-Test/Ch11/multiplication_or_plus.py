import pytest


@pytest.mark.parametrize(
    's, expected',
    [('02984', 576),
     ('567', 210),
     ('019900999', 65610)]
)
def test_solve(s, expected):
    result = solve(s)
    assert result == expected


def solve(s):
    data = list(map(int, s))
    result = data[0]

    for i in range(1, len(data)):
        num = int(data[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result += num
    
    return result