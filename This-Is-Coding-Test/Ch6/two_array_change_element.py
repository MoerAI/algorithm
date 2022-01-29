import pytest

@pytest.mark.parametrize(
    'n, k, a, b, expected',
    [(5, 3,
      [1, 2, 5, 4, 3],
      [5, 5, 6, 6, 5],
      26)]
)
def test_solve(n, k, a, b, expected):
    result = solve(k, a, b)
    assert result == expected


def solve(k, a, b):
    a.sort()
    b.sort(reverse = True)

    # 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break

    return sum(a)

