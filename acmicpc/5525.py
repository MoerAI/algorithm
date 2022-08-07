# Problem
"""
N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.
- P1 IOI
- P2 IOIOI
- P3 IOIOIOI
- PN IOIOI...OI (O가 N개)
I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.

<제한>
1 ≤ N ≤ 1,000,000
2N+1 ≤ M ≤ 1,000,000
S는 I와 O로만 이루어져 있다.
"""

# Input
"""
첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.
"""

# Output
"""
S에 PN이 몇 군데 포함되어 있는지 출력한다.
"""

# Example
"""
|Input1|
1
13
OOIOIOIOIIOII
|Output1|
4

|Input2|
2
13
OOIOIOIOIIOII
|Output2|
2
"""

# Solution
n = int(input())
m = int(input())
s = input()

ans = 0
cnt = 0
stack = []

for i in range(m):
    if s[i] == "O":
        continue
    else:
        stack.append(i)

for i in range(1, len(stack)):
    if stack[i] - stack[i-1] == 2:
        cnt += 1
    else:
        cnt = 0

    if cnt >= n:
        ans += 1


print(ans)