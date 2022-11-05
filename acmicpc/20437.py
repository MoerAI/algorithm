# Problem
"""
작년에 이어 새로운 문자열 게임이 있다. 게임의 진행 방식은 아래와 같다.

알파벳 소문자로 이루어진 문자열 W가 주어진다.
양의 정수 K가 주어진다.
어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.
위와 같은 방식으로 게임을 T회 진행한다.
"""

# Input
"""
문자열 게임의 수 T가 주어진다. (1 ≤ T ≤ 100)
다음 줄부터 2개의 줄 동안 문자열 W와 정수 K가 주어진다. (1 ≤ K ≤ |W| ≤ 10,000) 
"""

# Output
"""
T개의 줄 동안 문자열 게임의 3번과 4번에서 구한 연속 문자열의 길이를 공백을 사이에 두고 출력한다.
만약 만족하는 연속 문자열이 없을 시 -1을 출력한다.
"""

# Example
"""
|Input1|
2
superaquatornado
2
abcdefghijklmnopqrstuvwxyz
5
|Output1|
4 8
-1

|Input2|
1
abaaaba
3
|Output2|
3 4
"""

# Solution
# 전형적인 문자열 탐색 문제
import sys
input = sys.stdin.readline

number = int(input())

def get_counts(seq):
    counts = {}
    for x in seq:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


def get_keys(dic, n):
    keys = []
    for k, i in dic.items():
        if i == n:
            keys.append(k)
    return keys


for _ in range(number):
    s = input()
    n = int(input())
    counts = get_counts(list(s))
    if n in counts:
        keys = get_keys(counts, n)
        for k in keys:
            s.find(k)

    else:
        print("-1")

# 출처 : https://hyunse0.tistory.com/288
import sys
from collections import defaultdict

'''
superaquatornado
2
'''

def string_game(string):
    len_str = len(string)

    # K개 이상 있는 문자만 따로 저장
    alpha = defaultdict(list)
   
    for i in range(len_str):
        if string.count(string[i]) >= K:
            alpha[string[i]].append(i)
    # alpha = {'u': [1, 7], 'r': [4, 11], 'a': [5, 8, 13], 'o': [10, 15]}

    # K개 이상 있는 문자가 없다면 -1
    if not alpha:
        return (-1,)
    
    # K개 이상 있는 문자에 대해 문자열 게임 진행
    min_str = 10000
    max_str = 0

    for idx_lst in alpha.values():
        for j in range(len(idx_lst)-K+1):
            temp = idx_lst[j+K-1] - idx_lst[j] + 1

            if temp < min_str:
                min_str = temp

            if temp > max_str:
                max_str  = temp
    
    return min_str, max_str


T = int(sys.stdin.readline())

for t in range(1, T+1):
    string = sys.stdin.readline().strip()
    K = int(sys.stdin.readline())

    print(*string_game(string))