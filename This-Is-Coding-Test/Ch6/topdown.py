import pytest

@pytest.mark.parametrize(
    'count, inputs, expected',
    [(3,
      [15, 27, 12],
      [27, 15, 12])])
def test_solve(num, array, expected):
    result = solve(num, array)
    assert result == expected

def solve(num, array):

    return sorted(array, reverse = True)