import pytest
# 행복 왕국의 왕실 정원은 체스판과 같은 8 X 8 좌표 평면이다. 왕실 정원의 특정한 한 칸에 나이트가 서 있다.
# 나이트는 매우 충성스러운 신하로서 매일 무술을 연마한다.
# 나이트는 말을 타고 있기 때문에 이동을 할 때는, L자 형태로만 이동할 수 있으며,
# 정원 밖으로는 나갈 수 없다. 나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.
# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
# 이처럼 8 X 8 좌표 평면상에서 나이트의 위치가 주어졌을 때,
# 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.
# 이 때, 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며,
# 열 위치를 표현 할 때는 a부터 h로 표현한다.

@pytest.mark.parametrize("coordinate, expected", [("a1", 2), ("d5", 8)])
def test_solve(coordinate, expected):
    result = solve_m(coordinate)
    assert result == expected

# 나의 풀이
def solve_m(coordinate):
    count = 8
    if "a" or "h" in coordinate:
        count = count - 4
    elif "b" or "g" in coordinate:
        count = count - 2

    if "1" or "8" in coordinate:
        if "a" or "h" in coordinate:
            count = count - 2
        elif "b" or "g" in coordinate:
            count = count - 1
        else:
            count = count - 4
    elif "2" or "7" in coordinate:
        if "a" or "h" in coordinate:
            count = count -2
        elif "b" or "g" in coordinate:
            count = count -2
        else:
            count = count - 2

    return count

# 교재 풀이 1
def solve1(coordinate):
    count = 0

    keys = ["a", "b", "c", "d", "e", "f", "g", "h"]

    x, y = keys.index(coordinate[0]) + 1, int(coordinate[1])

    movement = [(-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2), (-2, -1), (-2, 1)]

    for move in movement:
        dx, dy = x + move[0], y + move[1]
        if dx < 1 or dy < 1 or dx > 8 or dy > 8:
            continue
        count += 1

    return count

# 교재 풀이 2
def solve2(coordinate):
    row = int(coordinate[1])
    # ord : 문자의 유니코드 값
    column = int(ord(coordinate[0])) - int(ord('a')) + 1

    steps = [(-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2), (-2, -1), (-2, 1)]

    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]
        if 1 <= next_row <= 8 and 1 <= next_column <= 8:
            result += 1

    return result