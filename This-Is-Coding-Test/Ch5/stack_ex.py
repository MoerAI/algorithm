stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력

# 내 생각에 stack은 우리의 일반적인 타이핑을 연상하면 좋을거같다.
# 타이핑으로 입력하는 경우 나중에 쓴 글자가 가장 먼저 지워진다.