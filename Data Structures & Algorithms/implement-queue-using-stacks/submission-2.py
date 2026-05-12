class MyQueue:

    def __init__(self):
        self.s = None

    def push(self, x: int) -> None:
        self.s = deque([self.s, x])

    def pop(self) -> int:
        dp = self.s.pop()
        top = self.s.pop()
        self.s = dp
        return top

    def peek(self) -> int:
        return self.s[1]

    def empty(self) -> bool:
        return not self.s


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()