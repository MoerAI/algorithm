import pytest
@pytest.mark.parametrize(
    'n, array, expected',
    [4, [5, 1, 7, 9], 5]
)
def test(n, array, expected):
    result = solution(n, array)
    assert result == expected


def solution(n, array):
    return sorted(array)[n - 1] // 2