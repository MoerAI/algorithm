# leetcode 206 : Reverse Linked List
# 연결 리스트를 뒤집어라.
# input:  1->2->3->4->5->NULL
# output: 5->4->3->2->1->NULL

#재귀 구조로 뒤집기
def reverseList(self, head: ListNode) -> ListNode:
    def reserse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reserse(next, node)
    return reserse(head)

#반복 구조로 뒤집기
def reverseList(self, head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev