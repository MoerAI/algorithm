# Problem
"""
길이가 N으로 같은 문자열 X와 Y가 있을 때, 두 문자열 X와 Y의 차이는 X[i] ≠ Y[i]인 i의 개수이다.
예를 들어, X=”jimin”, Y=”minji”이면, 둘의 차이는 4이다.
두 문자열 A와 B가 주어진다.
이때, A의 길이는 B의 길이보다 작거나 같다.
이제 A의 길이가 B의 길이와 같아질 때 까지 다음과 같은 연산을 할 수 있다.
    1. A의 앞에 아무 알파벳이나 추가한다.
    2. A의 뒤에 아무 알파벳이나 추가한다.
이때, A와 B의 길이가 같으면서, A와 B의 차이를 최소로 하는 프로그램을 작성하시오.
"""

# Input
"""
첫째 줄에 A와 B가 주어진다. A와 B의 길이는 최대 50이고, A의 길이는 B의 길이보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.
"""

# Output
"""
A와 B의 길이가 같으면서, A와 B의 차이를 최소가 되도록 했을 때, 그 차이를 출력하시오.
"""

# Example
"""
|Input1|
adaabc aababbc
|Output1|
2

|Input2|
hello xello
|Output2|
1

|Input3|
koder topcoder
|Output3|
1

|Input4|
abc topabcoder
|Output4|
0

|Input5|
giorgi igroig
|Output5|
6
"""

# Solution
a, b = list(map(str, input().split(" ")))
answer = 0
answer_list = []
if len(a) == len(b):
    for i in range(len(a)):
        if a[i] != b[i]:
            answer += 1
    answer_list.append(answer)
else:
    n = len(b) - len(a)
    for i in range(n+1):
        for j in range(len(a)):
            if a[j] != b[i + j]:
                answer += 1
        answer_list.append(answer)
        answer = 0
print(min(answer_list))