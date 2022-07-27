# Problem
"""
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
"""

# Input
"""
첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.
"""

# Output
"""
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
"""

# Example
"""
|Input1|
2143
|Output1|
TAAGATAC
4321

|Input2|
999998999
|Output2|
999999998

|Input3|
61423
|Output3|
64321

|Input4|
500613009
|Output4|
965310000
"""

# Solution
n = str(input())
s = []
result = ''

for c in n:
    s.append(int(c))

s.sort(reverse=True)

for c in s:
    result += str(c)

print(result)