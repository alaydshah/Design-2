class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_1, self.stack_2 = [], []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
                
        return self.stack_2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        
        return self.stack_2[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not (self.stack_1 or self.stack_2)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()