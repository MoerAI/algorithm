# Problem
"""
문자열과 놀기를 세상에서 제일 좋아하는 영식이는 오늘도 문자열 2개의 LCS(Longest Common Subsequence)를 구하고 있었다.
어느 날 영식이는 조교들이 문자열 3개의 LCS를 구하는 것을 보았다.
영식이도 도전해 보았지만 실패하고 말았다.

이제 우리가 할 일은 다음과 같다.
영식이를 도와서 문자열 3개의 LCS를 구하는 프로그램을 작성하라.
"""

# Input
"""
첫 줄에는 첫 번째 문자열이, 둘째 줄에는 두 번째 문자열이, 셋째 줄에는 세 번째 문자열이 주어진다.
각 문자열은 알파벳 소문자로 이루어져 있고, 길이는 100보다 작거나 같다.
"""

# Output
"""
첫 줄에 첫 번째 문자열과 두 번째 문자열과 세 번째 문자열의 LCS의 길이를 출력한다.
"""

# Example
"""
|Input1|
abcdefghijklmn
bdefg
efg
|Output1|
1
"""

# Solution
import sys
input = sys.stdin.readline

f = input().strip()
s = input().strip()
t = input().strip()

fl = len(f)
sl = len(s)
tl = len(t)

dp = [[[-1] * tl for i in range(sl)] for j in range(fl)]

def LCS(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return 0

    if dp[a][b][c] == -1:
        dp[a][b][c] = 0

        if f[a] == s[b] == t[c]:
            dp[a][b][c] = LCS(a - 1, b - 1, c - 1) + 1
        else:
            dp[a][b][c] = max(max(LCS(a, b - 1, c), LCS(a - 1, b, c)), LCS(a, b, c - 1))

    return dp[a][b][c]

print(LCS(fl - 1, sl - 1, tl - 1))
