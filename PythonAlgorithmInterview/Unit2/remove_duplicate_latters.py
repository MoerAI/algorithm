# leetcode 316 : Remove Duplicate Letters
# 중복된 문자를 제외하고 사전식 순서(Lexicographical Order)로 나열하라
# input1:  "bcabc"
# output1: "abc"
# input2: "cbacdcbc"
# input2: "acdb"

# 재귀를 이용한 분리
def removeDuplicateLetters(self, s: str) -> str:
    # 집합으로 정렬
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        # 전체 집합과 접미사 집합이 일치할 때 분리 진행
        if set(s) == set(suffix):
            return char + self.removeDuplicateLetters(suffix.replace(char,''))
    return ''

#스택을 이용한 문자 제거
def removeDuplicateLetters(self, s: str) -> str:
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join(stack)C