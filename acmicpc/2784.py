# Problem
"""
6개의 단어가 주어졌을 때, 이를 가지고 가로 세로 퍼즐을 만드는 프로그램을 작성하시오.
단어 3개는 가로줄, 3개는 세로줄로 배치해야한다.
"""

# Input
"""
6개의 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 이 단어는 사전순으로 정렬되어 있다.
"""

# Output
"""
6개 단어를 3*3 가로 세로 퍼즐에 놓을 수 없다면 0을 출력한다. 그렇지 않다면, 3개 줄에 퍼즐을 출력한다.
만약 가능한 답이 여러개라면 사전순으로 앞서는 것을 출력한다.
사전순으로 비교를 할 때는, 모두 한 줄로 이어붙인 9개의 단어를 생각하면 된다.
"""

# Example
"""
|Input1|
ANA
ANA
DAR
DAR
RAD
RAD
|Output1|
DAR
ANA
RAD

|Input2|
EVO
HEP
HIR
IVA
PAD
ROD
|Output2|
HEP
IVA
ROD

|Input3|
AKO
CES
DOC
DON
ESI
KES
|Output3|
0
"""
# Soultion
from itertools import combinations, permutations


def main():
    word = []
    for i in range(6):
        word.append(input())
    wordIdx = [0, 1, 2, 3, 4, 5]
    cases = list(combinations(wordIdx, 3)) #가로를 뽑음
    answer = []
    for case in cases:
        assemble(case, word, answer)
    if len(answer) == 0:
        print(0)
    else:
        answer = sorted(answer)[0]
        for i in range(3):
            print(answer[i])


def assemble(case, word, answer):
    vertical = []
    for i in range(6):
        if i not in case:
            vertical.append(i)
    vPerm = list(permutations([0, 1, 2], 3))
    pPerm = list(permutations([0, 1, 2], 3))
    for vcase in vPerm:
        for pcase in pPerm:
            flag = 1 #이 케이스일때 가능한지 확인
            tmpP = [word[case[pcase[0]]], word[case[pcase[1]]], word[case[pcase[2]]]]
            tmpV = ['', '', '']
            for j in range(3):
                tmpW = word[vertical[vcase[j]]]
                for i in range(3):
                    tmpV[i] = tmpV[i] + tmpW[i]
            for i in range(3):
                for j in range(3):
                    if tmpP[i][j] != tmpV[i][j]:
                        flag = 0
            if flag:
                answer.append(tmpP)


if __name__ == '__main__':
    main()

# 출처 : https://github.com/Hal-ws/--Algorithm-Problem-Solving/commit/53688702c51dc6d08cec54c68de0dfff07505a0d
