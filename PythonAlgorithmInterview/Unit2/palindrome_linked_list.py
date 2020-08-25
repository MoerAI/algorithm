# leetcode 234 : Palindrome Linked List
# 연결 리스트가 팰린드롬 구조인지 판별하라
# input1:  1->2
# output1: false
# input2:  1->2->2->1
# output2: true

# 1. 리스트로 변환하여 풀이
def isPalindrome(self, head: ListNode) -> bool:
    q: List = []

    if not head:
        return True

    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    #팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True

# 데크를 이용한 최적화
def isPalindrome(self, head: ListNode) -> bool:
    # 데크 자료형 선언
    q: Deque = collections.deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True