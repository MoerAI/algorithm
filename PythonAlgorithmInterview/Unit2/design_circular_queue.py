# leetcode 6622 : Design Circular Queue
# 원형 큐를 디자인하라.
# MyCircularQueue circularQueue = new MyCircularQueue(5); //크기를 5로 지정
# circularQueue.enQueue(10); // true 리턴
# circularQueue.enQueue(20); // true 리턴
# circularQueue.enQueue(30); // ture 리턴
# circularQueue.enQueue(40); // ture 리턴
# circularQueue.Rear(); // 40 리턴
# circularQueue.isFull(); // false 리턴
# circularQueue.deQueue(); // true 리턴
# circularQueue.deQueue(); // true 리턴
# circularQueue.enQueue(50); // true 리턴
# circularQueue.enQueue(60); // true 리턴
# circularQueue.Rear(); // 60 리턴
# circularQueue.Front(); // 30 리턴

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0
    
    # enQueue(): 리어 포인터 이동
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False
    
    # deQueue(): 프론트 포인터 이동
    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.p1 == self.p2 and self.q[self.p1] is not None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()