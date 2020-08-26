# leetcode 92 : Reverse Linked List 2
# 인덱스 m에서 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.
# input:  1->2->3->4->5->NULL, m = 2, n = 4
# output: 1->4->3->2->5->NULL

#반복 구조로 노드 뒤집기
def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    # 예외처리
    if not head or m == n:
        return head

    root = start = ListNode(None)
    root.next = head
    # start, end 지정
    for _ in range(m - 1):
        start = start.next
    end = start.next

    #반복하면서 노드 차례대로 뒤집기
    for _ in range(n - m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
    return root.next