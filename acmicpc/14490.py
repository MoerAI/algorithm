# Problem
"""
대열이는 욱제의 친구다.
- “야 백대열을 약분하면 뭔지 알아?”
- “??”
- “십대일이야~ 하하!”
n:m이 주어진다. 욱제를 도와주자. (...)
"""

# Input
"""
n과 m이 :을 사이에 두고 주어진다. (1 ≤ n, m ≤ 100,000,000)
"""

# Output
"""
두 수를 최대한으로 약분하여 출력한다.
"""

# Example
"""
|Input1|
100:10
|Output1|
10:1

|Input2|
18:24
|Output2|
3:4
"""

# Solution
from math import gcd

n, m = map(int, input().split(':'))

num = gcd(n, m)

print(f"{n // num}:{m // num}")