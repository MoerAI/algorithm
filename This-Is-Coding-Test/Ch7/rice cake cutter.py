import pytest


@pytest.mark.parametrize(
    "n, m, array, expected",
    [(4, 6,
      [19, 15, 10, 17],
      15
      )])
def test_solve(n, m, array, expected):
    h = solve(m, array)
    assert h == expected

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) / 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)

def solve(m, array):
    start = 0
    end = max(array)

    h = binary_search(array, m, start, end)
    return h