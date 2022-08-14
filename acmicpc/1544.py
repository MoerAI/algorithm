# Problem
"""
사이클 단어는 어떤 단어를 원형 모양으로 차례대로 쓴 것이다.
따라서, 어떤 단어를 이렇게 쓴 후에 임의의 단어를 고른다. 그 후에 시계방향으로 차례대로 읽으면 그 것이 단어가 된다.
만약에 단어 A와 단어 B가 있을 때, 단어 B를 원형으로 써서, 단어 A와 같이 읽을 수 있으면, 두 단어는 같은 단어이다.
따라서, picture와 turepic은 같은 단어다.
N개의 단어가 주어졌을 때, 서로 다른 단어가 총 몇 개인지 구하는 프로그램을 작성하시오.
"""

# Input
"""
첫째 줄에 단어의 개수 N이 주어진다. 둘째 줄부터 단어가 한 줄에 하나씩 주어진다.
단어는 영어 소문자로만 이루어져 있다. N은 50보다 작거나 같은 자연수이며, 단어의 길이는 최대 50이다.
"""

# Output
"""
첫째 줄에 서로 다른 단어가 몇 개인지 출력한다.
"""

# Example
"""
|Input1|
5
picture
turepic
icturep
word
ordw
|Output1|
2

|Input2|
7
ast
ats
tas
tsa
sat
sta
ttt
|Output2|
3
"""
# Soultion
from collections import deque

n = int(input())
words = []
for _ in range(n):
    words.append(input().rstrip())

for i in range(n):
    dq = deque(words[i])
    while True:
        dq.append(dq.popleft())
        save = "".join(dq)
        if save == words[i]:
            break
        if save in words:
            idx = words.index(save)
            words.pop(idx)
            words.insert(idx, words[i])
        
words = set(words)
print(len(words))