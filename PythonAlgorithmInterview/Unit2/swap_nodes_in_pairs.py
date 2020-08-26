# leetcode 24 : Swap Nodes in Pairs
# 연결 리스트를 입력받아 페어 단위로 스왑하라.
# input:  1->2->3->4
# output: 2->1->4->3

#1. 값만 교환하여 풀이(직관적이지만 문제가 의도하는 풀이와 다른 풀이)
def swapPairs(self, head: ListNode) -> ListNode:
    cur = head

    while cur and cur.next:
        # 값만 교환
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return head

#2. 반복 구조로 스왑
def swapPairs(self, head: ListNode) -> ListNode:
    root = prev = ListNode(None)
    prev.next = head
    while head and head.next:
        b = head.next
        head.next = b.next
        b.next = head

        # prev가 b를 가리키도록 할당
        prev.next = b

        # 다음번 비교를 위해 이동
        head = head.next
        prev = prev.next.next

    return root.next

#3. 제귀 구조로 스왑
def swapPairs(self, head: ListNode) -> ListNode:
    if head and head.next:
        p = head.next
        # 스왑된 값 리턴 받음
        head.next = self.swapPairs(p.next)
        p.next = head
        return p
    return head