import pytest
# 여행가 A는 N X N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 X 1 크기의 정사각형으로 나누어져 있다.
# 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다.
# 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다.
# 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있다.
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 적혀있다.
# 각 문자의 의미는 다음과 같다.
# L: 왼쪽으로 한 칸 이동 # R: 오른쪽으로 한 칸 이동 # U: 위로 한 칸 이동 # D: 아래로 한 칸 이동
# 이 때 여행가 A가 N X N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
# 공간의 크기 N이 주어지고 이동 방향 리스트가 주어진다.

@pytest.mark.parametrize("n, plans, expected", [(5, "R R R U D D", "3 4")])
def test_solve(n, plans, expected):
    result = solve_m(n, plans)
    assert result == expected

# 나의 풀이
def solve_m(n, plans):
    row = 1
    col = 1
    for direction in plans:
        if direction == 'L' & row > 1:
            row = row - 1
        elif direction == 'R' & row < n:
            row = row + 1
        elif direction == 'U' & col > 1:
            col = col - 1
        elif direction == 'D' & col < n:
            col = col + 1

    return str(col, row)


# 교재 풀이 1
def solve1(n, plans):
    result = (1, 1)

    directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

    for plan in plans.split():
        move = directions.get(plan)
        new = (result[0] + move[0], result[1] + move[1])
        if new[0] < 1 or new[0] > n or new[1] < 1 or new[1] > n:
            continue
        result = new

    return str(result[0]) + " " + str(result[1])


# 교재 풀이 2
def solve2(n, plans):
    nx, ny = 0, 0
    x, y = 1, 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for plan in plans.split():
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny

    return str(x) + ' ' + str(y)