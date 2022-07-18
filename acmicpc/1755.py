# Problem
"""
79를 영어로 읽되 숫자 단위로 하나씩 읽는다면 "seven nine"이 된다.
80은 마찬가지로 "eight zero"라고 읽는다.
79는 80보다 작지만, 영어로 숫자 하나씩 읽는다면 "eight zero"가 "seven nine"보다 사전순으로 먼저 온다.
문제는 정수 M, N(1 ≤ M ≤ N ≤ 99)이 주어지면 M 이상 N 이하의 정수를 숫자 하나씩 읽었을 때를 기준으로 사전순으로 정렬하여 출력하는 것이다.
"""

# Input
"""
첫째 줄에 M과 N이 주어진다.
"""

# Output
"""
M 이상 N 이하의 정수를 문제 조건에 맞게 정렬하여 한 줄에 10개씩 출력한다.
"""

# Example
"""
|Input1|
8 28
|Output1|
8 9 18 15 14 19 11 17 16 13
12 10 28 25 24 21 27 26 23 22
20
"""

# Solution
n, m = list(map(int, input().split(" ")))

dic = {"1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine", "0":"zero"}
num_list = []

for i in range(n,m+1):
    num = ''.join(dic[c] for c in str(i))
    num_list.append([i, num])

num_list.sort(key=lambda x:x[1])

for i in range(len(num_list)):
    if i % 10 == 0 and i != 0:
        print()
    print(num_list[i][0], end=' ')