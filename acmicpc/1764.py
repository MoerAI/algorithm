# Problem
"""
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
"""

# Input
"""
첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.
이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.
이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.
듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.
"""

# Output
"""
듣보잡의 수와 그 명단을 사전순으로 출력한다.
"""

# Example
"""
|Input|
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
|Output|
2
baesangwook
ohhenrie
"""

# Solution
n, m = map(int, input().split(' '))

names1 = set()
for _ in range(n):
    names1.add(input())

names2 = set()
for _ in range(m):
    names2.add(input())

names3 = sorted(list(names1 & names2))
print(len(names3))
for name in names3:
    print(name)