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

