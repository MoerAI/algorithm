# Problem
"""
임한수와 임문빈은 서로 사랑하는 사이이다.
임한수는 세상에서 팰린드롬인 문자열을 너무 좋아하기 때문에, 둘의 백일을 기념해서 임문빈은 팰린드롬을 선물해주려고 한다.
임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데, 임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.
임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성하시오.
"""

# Input
"""
첫째 줄에 임한수의 영어 이름이 있다. 알파벳 대문자로만 된 최대 50글자이다.
"""

# Output
"""
첫째 줄에 문제의 정답을 출력한다. 만약 불가능할 때는 "I'm Sorry Hansoo"를 출력한다.
정답이 여러 개일 경우에는 사전순으로 앞서는 것을 출력한다.
"""

# Example
"""
|Input1|
AABB
|Output1|
ABBA

|Input2|
AAABB
|Output2|
ABABA

|Input3|
ABACABA
|Output3|
AABCBAA

|Input4|
ABCD
|Output4|
I'm Sorry Hansoo
"""

# Solution
s = input()
dic = {}
odd = ''
result = ''
cnt = 0
for c in s:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1

for c in dic:
    if dic[c] % 2 == 1:
        cnt += 1
        odd = c
        if cnt == 2:
            print("I'm Sorry Hansoo")
            exit()

dic_sort = sorted(dic)

for c in dic_sort:
    i = int(dic[c] / 2)
    result += i*c

re_result = result[::-1]
result = result + odd + re_result
print(result)