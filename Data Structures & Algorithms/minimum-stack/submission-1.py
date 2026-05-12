class MinStack:

    def __init__(self):
        self.s = []    
        self.minStack = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.minStack:
            self.minStack.append(val if val <= self.minStack[-1] else self.minStack[-1])

    def pop(self) -> None:
        self.minStack.pop()
        return self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
