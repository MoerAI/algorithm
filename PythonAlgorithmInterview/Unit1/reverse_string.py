#leetcode 344 : Reverse String
#문자열을 뒤집는 함수를 작성하여라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.
#1. 포인터를 이용한 스왑
def reverseString1(self, s: List[str]) -> None:
    left, right = 0, len(s) -1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

#2. 파이썬 내장함수 사용
def reverseString2(self, s: List[str]) -> None:
    s.reverse()
