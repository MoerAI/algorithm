# Problem
"""
동호와 규완이는 212호에서 문자열에 대해 공부하고 있다.
규완이는 팰린드롬을 엄청나게 좋아한다.
팰린드롬이란 앞에서부터 읽으나 뒤에서부터 읽으나 같게 읽히는 문자열을 말한다.
동호는 규완이를 위한 깜짝 선물을 준비했다.
동호는 규완이가 적어놓고 간 문자열 S에 0개 이상의 문자를 문자열 뒤에 추가해서 팰린드롬을 만들려고 한다.
동호는 가능하면 가장 짧은 문자열을 만들려고 한다.
동호가 만들 수 있는 가장 짧은 팰린드롬의 길이를 출력하는 프로그램을 작성하시오.
"""

# Input
"""
첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 최대 50이다.
"""

# Output
"""
첫째 줄에 동호가 만들 수 있는 가장 짧은 팰린드롬의 길이를 출력한다.
"""

# Example
"""
|Input1|
abab
|Output1|
5

|Input2|
abacaba
|Output2|
7

|Input3|
qwerty
|Output3|
11

|Input4|
abdfhdyrbdbsdfghjkllkjhgfds
|Output4|
38
"""

# Solution
import sys

s = str(input = sys.stdin.readline)

if len(s)<2 or s==s[::-1]:
    print(len(s))
else:
    for i in range(len(s),0,-1):
        if s[i:len(s)]==s[len(s)-1:i-1:-1]:
            p = s[len(s)-1:i-1:-1]
    print(2 * len(s) - len(p))