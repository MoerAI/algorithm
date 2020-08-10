#leetcode 125 : Valid Palndrome
#주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
#1. 리스트로 변환
def isPalindrome(self, s: str) -> bool:
    #대소문자 전처리
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    #팰린프롬 여부를 판별        
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

#2 데크자료형으로 최적화
def isPalindrome(self, s: str) -> bool:
    #자료형 데크로 선언
    strs: Deque = collections.deque()
        
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
            
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
        
    return True

#3 슬라이싱 사용
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    #정규식으로 불필요한 문자 필터링
    s = re..sub('[^a-z0-9]', '',s)
    
    return s == s[::-1] #슬라이싱