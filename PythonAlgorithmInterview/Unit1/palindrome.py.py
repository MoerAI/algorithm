#1번풀이
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

#2번풀이
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

#3번풀이
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    #정규식으로 불필요한 문자 필터링
    s = re..sub('[^a-z0-9]', '',s)
    
    return s == s[::-1] #슬라이싱