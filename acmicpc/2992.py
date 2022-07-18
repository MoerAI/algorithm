# Problem
"""
정수 X가 주어졌을 때, X와 구성이 같으면서 X보다 큰 수 중 가장 작은 수를 출력한다.
수의 구성이 같다는 말은, 수를 이루고 있는 각 자리수가 같다는 뜻이다.
예를 들어, 123과 321은 수의 구성이 같다. 하지만, 123과 432는 구성이 같지 않다.
"""

# Input
"""
첫째 줄에 X가 주어진다. (1 ≤ X ≤ 999999) X는 0으로 시작하지 않는다.
"""

# Output
"""
첫째 줄에 결과를 출력한다. 만약 그러한 숫자가 없는 경우에는 0을 출력한다.
"""

# Example
"""
|Input1|
156
|Output1|
165

|Input2|
330
|Output2|
0

|Input3|
27711
|Output3|
71127
"""

# Solution
from itertools import permutations
n = input()
permu = (sorted(set(map(lambda x: ''.join(x), permutations(n, len(n))))))
print(0) if permu[-1] == n else print(permu[permu.index(n) + 1])