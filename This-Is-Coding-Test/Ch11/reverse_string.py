import pytest


@pytest.mark.parametrize(
    'data, expected',
    [('0001100', 1), ('101010', 3), ('1111', 0)]
)
def test_solve(data, expected):
    result = solution(data)
    assert result == expected


def solution(data):
    count0 = 0 # 전부 0으로 바꾸는 경우
    count1 = 0 # 전부 1로 바꾸는 경우

    if data[0] == '1':
        count0 += 1
    else:
        count1 += 1

    for i in range(len(data) - 1):
        if data[i] != data[i + 1]:
            if data[i + 1] == '1':
                count0 += 1
            else:
                count1 += 1
    
    return min(count0, count1)