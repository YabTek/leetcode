from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.temp = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.temp:
            self.temp.append(val)
        elif val <= self.temp[-1]:
            self.temp.append(val)
        return self.stack.append(val)
        
    def pop(self) -> None:
        if self.stack.pop() == self.temp[-1]:
            self.temp.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.temp[len(self.temp)-1]
        