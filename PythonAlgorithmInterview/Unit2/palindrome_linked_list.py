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

#런너 테크닉을 이용한 우하한 풀이
def isPalindrome(self, head: ListNode) -> bool:
    rev = None
    slow = fast = head
    #런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    #팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev