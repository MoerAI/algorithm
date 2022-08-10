# Problem
"""
만약 어떤 단어A를 숌스럽게 바꿔서 또다른 단어 B로 만든다면, 그 단어는 비슷한 단어라고 한다.
어떤 단어를 숌스럽게 바꾼다는 말은 단어 A에 등장하는 모든 알파벳을 다른 알파벳으로 바꾼다는 소리다.
그리고, 단어에 등장하는 알파벳의 순서는 바뀌지 않는다.
두 개의 다른 알파벳을 하나의 알파벳으로 바꿀 수 없지만, 자기 자신으로 바꾸는 것은 가능하다.
예를 들어, 단어 abca와 zbxz는 비슷하다. 그 이유는 a를 z로 바꾸고, b는 그대로 b, c를 x로 바꾸면, abca가 zbxz가된다.
단어가 여러 개 주어졌을 때, 몇 개의 쌍이 비슷한지 구하는 프로그램을 작성하시오.
"""

# Input
"""
첫째 줄에 단어의 개수 N이 주어진다. 둘째 줄부터 N개의 줄에 한 줄에 하나씩 단어가 주어진다.
단어의 길이는 최대 50이고, N은 100보다 작거나 같은 자연수이다.
모든 단어의 길이는 같고, 중복되지 않는다. 또, 알파벳 소문자로만 이루어져 있다.
"""

# Output
"""
첫째 줄에 총 몇 개의 쌍이 비슷한지 출력한다.
"""

# Example
"""
|Input1|
5
aa
ab
bb
cc
cd
|Output1|
4

|Input2|
3
abca
zbxz
opqr
|Output2|
1

|Input3|
12
cacccdaabc
cdcccaddbc
dcdddbccad
bdbbbaddcb
bdbcadbbdc
abaadcbbda
babcdabbac
cacdbaccad
dcddabccad
cacccbaadb
bbcdcbcbdd
bcbadcbbca
|Output3|
13
"""

# Solution
# 문자열을 전부 다 바꿔주고 비교하기

# Solution
n=int(input())
list=[input() for _ in range(n)]
cnt=0
for i in range(0,n-1) :
    for j in range(i+1,n) :
        s1=list[i]
        s2=list[j]
        flag =True
        if len(s1)==len(s2):
            visit1=[0]*26
            visit2=[0]*26
            for k in range(len(s1)):
                idx1=ord(s1[k])-ord('a')
                idx2=ord(s2[k])-ord('a')
                
                if visit1[idx1]==0 and visit2[idx2]==0:
                    visit1[idx1]=s2[k]
                    visit2[idx2]=s1[k]
                elif visit1[idx1]!=s2[k]:
                    flag=False
                    break
        if flag:
            cnt+=1        
print(cnt)