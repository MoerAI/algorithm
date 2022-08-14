# Problem
"""
크로스워드 퍼즐은 R*C크기의 직사각형으로 이루어져 있고, 각 칸은 비어있거나 막혀있다.
퍼즐은 가로(왼쪽->오른쪽) 또는 세로(위->아래)로 연속된 빈 칸에 단어를 채우면서 푼다.
동혁이는 크로스워드 퍼즐을 풀지 않는다.
그는 풀려있는 퍼즐을 쳐다본다.
그런 후에, 그는 그 퍼즐에서 사전순으로 제일 앞서는 단어를 찾는다. (단어는 적어도 2글자이다.)
크로스워드 퍼즐이 주어졌을 때, 사전순으로 제일 앞서는 단어를 출력하는 프로그램을 작성하시오.
"""

# Input
"""
첫째 줄에 R과 C (2 ≤ R, C ≤ 20)가 주어진다. R는 행의 개수, C는 열의 개수이다.
그 다음 R개의 줄엔 C개의 문자가 포함되어 있다.
각 문자는 영어 알파벳 소문자 또는 '#'이며, '#'인 경우에는 막혀있는 것이다.
"""

# Output
"""
첫째 줄에 사전순으로 제일 앞서는 단어를 출력한다. 정답이 항상 존재하는 경우만 입력으로 주어진다.
"""

# Example
"""
|Input1|
4 4
luka
o#a#
kula
i#a#
|Output1|
kala

|Input2|
4 4
luka
o#a#
kula
i#as
|Output2|
as

|Input3|
4 5
adaca
da##b
abb#b
abbac
|Output3|
abb
"""
# Soultion
r, c = map(int, input().split())
cross = []
result = []
for _ in range(r):
    s = input()
    cross.append(s)

for s in cross:
    result.extend(s.split('#'))

# list(zip(*cross))
for i in range(c):
    word = ''
    for j in range(r):
        word += cross[j][i]
    result.extend(word.split('#'))

result = list(filter(lambda x: len(x) > 1, result))
print(sorted(result)[0])