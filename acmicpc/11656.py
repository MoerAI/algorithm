# Problem
"""
접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬해 놓은 배열이다.
baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지가 있고,
이를 사전순으로 정렬하면, aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon이 된다.
문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성하시오.
"""

# Input
"""
첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000보다 작거나 같다.
"""

# Output
"""
aekjoon
baekjoon
ekjoon
joon
kjoon
n
on
oon
"""

# Example
"""
|Input|
baekjoon
|Output|
aekjoon
baekjoon
ekjoon
joon
kjoon
n
on
oon
"""
# Solution
s = input()
result = []

for i in range(len(s)):
    result.append(s[i:])

result.sort()
for c in result:
    print(c)