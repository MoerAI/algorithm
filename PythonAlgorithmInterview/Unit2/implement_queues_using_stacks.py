# leetcode 232 : Implement Queue Using Stacks
# 스택을 이용해 다음 연산을 지원하는 큐를 구현하라.
# push(x): 요소 x를 큐 마지막에 삽입한다.
# pop(): 큐 처음에 있는 요소를 제거한다.
# peek(): 큐 처음에 있는 요소를 조회한다.
# empty(): 큐가 비어 있는지 여부를 리턴한다.
# MyQueue queue = new MyQueue();
# queue.push(1);
# queue.push(2);
# queue.peek(); // 1 리턴
# queue.pop(); // 1 리턴
# queue.empty() // false 리턴

# 스택 2개 사용
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        # ouput이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
    
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.input == [] and self.output == []    


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()