# leetcode 328 : Odd Even Linked List
# 연결 리스트를 홀수 노드에 짝수 노드가 오도록 재구성하라. 공간 복잡도 O(1), 시간 복잡도 O(n)에 풀이하라.
# input1:  1->2->3->4->5->NULL
# output1: 1->3->5->2->4->NULL
# input2:  2->1->3->5->6->4->7->NULL
# output2: 2->3->6->7->1->5->4->NULL

# 반복 구조로 홀짝 노드 처리
def oddEvenList(self, head: ListNode) -> ListNode:
    # 예외처리
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    #반복하면서 홀짝 노드 처리
    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    #홀수 노드의 마지막을 짝수 헤드로 연결
    odd.next = even_head
    return head