# Problem
"""
꿀벌이 하는 일은 다음과 같이 분류할 수 있다.
휴식(Re), 순찰(Pt), 방청소(Cc), 꽃가루 먹기(Ea), 새끼 돌보기(Tb), 벌집 짓기와 관리(Cm), 외부 활동(Ex)
한 꿀벌이 1시간 동안 한 일이 주어졌을 때, 각각을 몇 번 했고, 비율이 어떻게 되는지 구하는 프로그램을 작성하시오.
"""

# Input
"""
입력은 꿀벌이 한 일이 공백과 줄바꿈으로 구분되어서 주어진다. 최대 24개의 일을 한다.
"""

# Output
"""
각각의 일을 한 횟수와 비율을 공백으로 구분하여 출력한다.
출력은 {Re,Pt,Cc,Ea,Tb,Cm,Ex} 순서대로 하며, 비율은 소수점 둘째 자리까지 출력한다.
주어진 목록에 없는 일은 출력하지 않는다.
입력의 마지막 줄에는 "Total <total> 1.00"을 출력하며, <total>은 꿀벌이 한 일의 개수이다.
"""

# Example
"""
|Input1|
Cc Pt Pt Re Tb Re Cm Cm Re Pt Pt Re Ea Ea Pt Pt
Pt Re Re Cb Cb Pt Pt Cb
|Output1|
Re 6 0.25
Pt 9 0.38
Cc 1 0.04
Ea 2 0.08
Tb 1 0.04
Cm 2 0.08
Ex 0 0.00
Total 24 1.00
"""

# Solution
import sys
dic = {"Re":0,"Pt":0,"Cc":0,"Ea":0,"Tb":0,"Cm":0,"Ex":0}
x = ''
works = []
cnt = 0

for line in iter(input, x):
    works.append(line)

for l in range(len(works)):
    for work in works[l].split(' '):
        if work in dic:
            dic[work] += 1
            cnt += 1

for work in dic:
    print(dic[work])