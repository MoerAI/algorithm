import pytest


@pytest.mark.parametrize(
    "n, array, m, parts, expected",
    [(5,
      [8, 3, 7, 9, 2],
      3,
      [5, 7, 9],
      "no yes yes"
      )])
def test_solve(n, array, m, parts, expected):
    result = solve(n, array, parts)
    assert result == expected


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


def solve(n, array, parts):
  array.sort()
  result = ""
  x = list(map(int, input().split()))

  for part in parts:
    finding = binary_search(array, part, 0, n - 1)
    if finding is None:
      result += "no "
    else:
      result += "yes "