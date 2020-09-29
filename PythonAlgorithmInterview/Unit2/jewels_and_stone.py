# leetcode 771 : Jewels and Stones
# J는 보석이며, S는 보석을 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까? 대소문자는 구분한다.
# input  : J = "aA", S = "aAAbbbbb"
# output : 3

class Solution:
    # 해시 테이블을 이용한 풀이
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = {}
        count = 0
        
        #돌(S)의 빈도 수 계산
        for char in S:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1
        #보석의 빈도 수 합
        for char in J:
            if char in freqs:
                count += freqs[char]
                
        return count
    
    