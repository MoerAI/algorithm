# Problem
"""
국렬이는 신촌 연합 프로그래밍 경진대회에서 '독특한 계산기'를 Div 1 no solve 방지 문제로 냈다가 생각보다 많이 풀리지 않아서 정말 많이 반성하였다. 그 때문에 해당 문제보다 (출제자인 국렬이 기준으로) 더 쉬운 문제를 냈다. 물론 더 쉬울지 어려울지는 대회에 나와봐야 안다.

뒤집힌 계산기는 독특한 계산기의 동생이다. 동생인 만큼 뒤집힌 계산기의 계산 방법은 형보다 더 단순한 계산 방법을 가지고 있다.

  - 수식은 뒤에서 앞으로 계산한다.
  - 연산자의 계산 또한 뒤에서 앞으로 계산한다. 예를 들어서, 1-2는 2에서 1을 뺐기 때문에 1이다.
  - 연산자 우선순위 또한 바뀌어 있다.
수식은 숫자와 연산자가 교대로 나오며, 숫자로 시작해 숫자로 끝난다. 뒤집힌 계산기의 숫자는 인성이 나쁜 독특한 계산기와는 달리 음이 아닌 양의 정수이다. 즉 `-1-1`이나 `-1+-1`은 유효하지 않은 수식이다. 다만 그 형에 그 동생인지라 `001+0002`처럼 숫자의 앞에 불필요한 0이 있을 수 있다. 뒤집힌 계산기의 연산자는 +, -, *, / 중 하나이다. 각각 C++에서 정수 간에 정의된 덧셈, 뺄셈, 곱셈, 나눗셈을 의미한다. C++에서 나눗셈은 나누어지는 수가 양수면 나머지가 0 이상, 음수면 나머지가 0 이하로 처리하여 나오는 몫을 계산한다. 예를 들어, 3 / 2 = 1, (−3) / 2 = −1, 3 / (−2) = −1, (−3) / (−2) = 1로 계산된다.

이와 같은 계산 과정에 따라 주어진 식을 계산하시오.
"""

# Input
"""
다음과 같이 입력이 주어진다.
p1 p2 p3 p4
S

제한
1 ≤ pi ≤ 4 (1 ≤ i ≤ 4)
pi ≠ pj (1 ≤ i < j ≤ 4)
p1, p2, p3, p4는 각각 +, -, *, /의 우선순위를 나타낸다. 숫자가 높을수록 우선순위가 높다.
S는 계산하고자 하는 수식으로 지문에서 언급된 숫자와 연산자가 다른 문자 없이 교대로 나오며, 길이는 106 이하이다.
계산 과정 중의 모든 수는 −263 이상 263 미만이며, 0으로 나누는 경우는 없다. 숫자 앞에 불필요한 0이 있을 수 있다.
"""

# Output
"""
주어진 식을 계산한 결과를 출력한다. 불필요한 0은 제거해야 한다.
"""

# Example
"""
|Input1|
1 2 3 4
3*2+5-5+7
|Output1|
13
"""

# Solution
