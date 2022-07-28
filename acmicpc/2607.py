# Problem
"""
영문 알파벳 대문자로 이루어진 두 단어가 다음의 두 가지 조건을 만족하면 같은 구성을 갖는다고 말한다.
두 개의 단어가 같은 종류의 문자로 이루어져 있다.
같은 문자는 같은 개수 만큼 있다.
예를 들어 "DOG"와 "GOD"은 둘 다 'D', 'G', 'O' 세 종류의 문자로 이루어져 있으며 양쪽 모두 'D', 'G', 'O' 가 하나씩 있으므로
이 둘은 같은 구성을 갖는다. 하지만 "GOD"과 "GOOD"의 경우 "GOD"에는 'O'가 하나, "GOOD"에는 'O'가 두 개 있으므로 이 둘은 다른 구성을 갖는다.
두 단어가 같은 구성을 갖는 경우, 또는 한 단어에서 한 문자를 더하거나, 빼거나,
하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우에 이들 두 단어를 서로 비슷한 단어라고 한다.
예를 들어 "DOG"와 "GOD"은 같은 구성을 가지므로 이 둘은 비슷한 단어이다.
또한 "GOD"에서 'O'를 하나 추가하면 "GOOD" 과 같은 구성을 갖게 되므로 이 둘 또한 비슷한 단어이다.
하지만 "DOG"에서 하나의 문자를 더하거나, 빼거나, 바꾸어도 "DOLL"과 같은 구성이 되지는 않으므로 "DOG"과 "DOLL"은 비슷한 단어가 아니다.
입력으로 여러 개의 서로 다른 단어가 주어질 때,
첫 번째 단어와 비슷한 단어가 모두 몇 개인지 찾아 출력하는 프로그램을 작성하시오.
"""

# Input
"""
첫째 줄에 종이의 줄의 개수 N이 주어진다. (1 ≤ N ≤ 100)
다음 N개의 줄에는 각 줄의 내용이 주어진다. 각 줄은 최대 100글자이고, 항상 알파벳 소문자와 숫자로만 이루어져 있다.
"""

# Output
"""
종이에서 찾은 숫자의 개수를 M이라고 하면, 출력은 M줄로 이루어져야 한다.
각 줄에는 종이에서 찾은 숫자를 하나씩 출력해야 한다. 이때, 비내림차순으로 출력해야 한다.
비내림차순은 내림차순의 반대인 경우인데, 다음 수가 앞의 수보다 크거나 같은 경우를 말한다.
"""

# Example
"""
|Input1|
2
lo3za4
01
|Output1|
1
3
4

|Input2|
4
43silos0
zita002
le2sim
231233
|Output2|
0
2
2
43
231233

|Input3|
4
01bond
02james007
03bond
04austinpowers000
|Output3|
0
1
2
3
4
7
"""

# Solution
import re

n = int(input())
lan_list = []
numbers = []

for i in range(n):
    lan_list.append(input())

for s in lan_list:
    number = re.findall(r'\d+', s)
    numbers += number

numbers = list(map(int, numbers))
numbers = list(numbers)
numbers.sort()
for n in numbers:
    print(n)