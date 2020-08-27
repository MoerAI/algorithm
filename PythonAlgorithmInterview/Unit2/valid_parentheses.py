# leetcode 20 : Calid Parentheses
# 괄호로 된 입력값이 올바른지 판별하라.
# input:  ()[]{}
# output: True

#1. 스택 일치 여부를 판별하여 푼다.
def isValid(self, s: str) -> bool:
    stack = []
    table = {
        ')' : '(',
        ']' : '[',
        '}' : '{',
    }

    #스택 이용 예외 처리 및 일치 여부 판별
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0