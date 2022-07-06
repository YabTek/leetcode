from collections import deque

class MyQueue:

    def __init__(self):
        self.queue_in = deque()
        
    def push(self, x: int) -> None:
        return self.queue_in.append(x)

    def pop(self) -> int:
        return self.queue_in.popleft()

    def peek(self) -> int:
        return self.queue_in[0]
      
    def empty(self) -> bool:
        if len(self.queue_in) == 0:
            return True
        else:
            return False
        

