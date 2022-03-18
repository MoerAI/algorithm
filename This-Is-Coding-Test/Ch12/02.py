import pytest


@pytest.mark.parametrize(
    's, expected',
    [('K1KA5CB7', 'ABCKK13'), ('AJKDLSI412K4JSJ9D', 'ADDIJJJKKLSS20')]
)
def test(s, expected):
    result = solution(s)
    assert result == expected


def solution(s):
    result = ''
    num = 0

    s = sorted(s, key=lambda x: ord(x))

    for c in s:
        if ord(c) < ord('A'):
            num += int(c)
        else:
            result += c

    return result + str(num)


def solution2(data):

    result = []
    
    for x in data:
        # 알파벳인 경우 결과 리스트에 삽입
        if x.isalpha():
            result.append(x)
        # 숫자는 따로 더하기
        else:
            value += int(x)

    # 알파벳을 오름차순으로 정렬
    result.sort()

    # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
    if value != 0:
        result.append(str(value))

    # 최종 결과 출력(리스트를 문자열로 변환하여 출력)
    return ''.join(result)