import pytest

@pytest.mark.parametrize(
    'n, input, expected',
    [(2,
      ['홍길동 95', '이순신 77'],
      ['이순신', '홍길동'])])
def test_solve(n, input, expected):
    result = solve(input)
    assert result == expected

def solve(input):
    array = []
    result = []
    for i in input:
        data = i.split()
        array.append([data[0], int(data[1])])

    # 키(Key)를 이용하여, 점수를 기준으로 정렬
    array = sorted(array, key=lambda student: student[1])
    for student in array:
        result.append(student[0])
    return result