# 주어진 문자열의 부분 문자열 중 팰린드롬의 최대길이
s = input()

def solution(s):

    # 팰린드롬 판별 및 투포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    # 그 자체가 팰린드롬인 경우
    if len(s) <2 or s == s[::-1]:
        return len(s)

    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key = len)
    return len(result)

solution(s)