# Problem
"""
세 개의 단어가 주어졌을때, 꿍은 첫 번째 단어와 두 번째 단어를 섞어서 세 번째 단어를 만들 수 있는지 궁금해졌다. 첫 번째와 두 번째 단어는 마음대로 섞어도 되지만 원래의 순서는 섞여서는 안 된다. 다음과 같은 경우를 생각해보자.

    - 첫 번째 단어 : cat
    - 두 번째 단어 : tree
    - 세 번째 단어 : tcraete

보면 알 수 있듯이, 첫 번째 단어와 두 번째 단어를 서로 섞어서 세 번째 단어를 만들 수 있다. 아래와 같이 두 번째 예를 들어보자.

    - 첫 번째 단어 : cat
    - 두 번째 단어 : tree
    - 세 번째 단어 : catrtee

이 경우 역시 가능하다. 그렇다면 "cat"과 "tree"로 "cttaree"를 형성하는건 불가능하다는걸 눈치챘을 것이다.
"""

# Input
"""
입력의 첫 번째 줄에는 1부터 1000까지의 양의 정수 하나가 주어지며 데이터 집합의 개수를 뜻한다.
각 데이터집합의 처리과정은 동일하다고 하자.
각 데이터집합에 대해, 세 개의 단어로 이루어져 있으며 공백으로 구분된다. 
든 단어는 대문자 또는 소문자로만 구성되어 있다.
세 번째 단어의 길이는 항상 첫 번째 단어와 두 번째 단어의 길이의 합이며 첫 번째 단어와 두 번째 단어의 길이는 1~200이다.
"""

# Output
"""
각 데이터집합에 대해 다음과 같이 출력하라.

만약 첫 번째 단어와 두 번째 단어로 세 번째 단어를 형성할 수 있다면
Data set n: yes
과 같이 출력하고 만약 아니라면
Data set n: no
과 같이 출력하라. 물론 n은 데이터집합의 순번으로 바뀌어야 한다.
"""

# Example
"""
|Input1|
3
cat tree tcraete
cat tree catrtee
cat tree cttaree
|Output1|
Data set 1: yes
Data set 2: yes
Data set 3: no

"""

# Solution
# 각 단어 알파뱃 하나씩 대입하면서 3번째 단어랑 맞는지 확인한다.
import sys
input = sys.stdin.readline
from collections import deque

def bfs(words):
    A, B, C = words
    dq = deque([(len(A), len(B), len(C))])
    visited = [[0] * (len(B)+1) for _ in range(len(A)+1)]
    while dq:
        ai, bi, ci = dq.popleft()
        if ai == bi == ci == 0:
            return True
        elif ci == 0:
            return False

        if ai > 0 and A[ai-1] == C[ci-1] and visited[ai-1][bi] == 0:
            visited[ai-1][bi] = 1
            dq.append([ai-1, bi, ci-1])
        if bi > 0 and B[bi-1] == C[ci-1] and visited[ai][bi-1] == 0:
            visited[ai][bi-1] = 1
            dq.append([ai, bi-1, ci-1])
    else:
        return False

n = int(input())
for i in range(n):
    words = list(map(str, input().split()))
    if bfs(words):
        print("Data set %d: yes" %(i+1))
    else:
        print("Data set %d: no" %(i+1))

# 출처 : https://velog.io/@nkrang/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-9177-%EB%8B%A8%EC%96%B4-%EC%84%9E%EA%B8%B0-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC