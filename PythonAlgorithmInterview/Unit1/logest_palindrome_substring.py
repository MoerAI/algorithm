#leetcode 5 : Longest Palindrome Substring
#가장 긴 팰린드롬 부분 문자열을 출력하라
#input1  : "babad"
#output1 : "bab"(or "aba")
#input2  : "cbbd"
#output2 : "bb"

def longestPalindrome(self, s: str) -> str:
    #팰린드롬 판별 및 투포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1 
            right += 1 
        return s[left + 1:right - 1]
    
    if len(s) <2 or s == s[::-1]:
        return s
    
    result=''
    
    #슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1),
                             expand(i, i + 2),
                             key=len)
