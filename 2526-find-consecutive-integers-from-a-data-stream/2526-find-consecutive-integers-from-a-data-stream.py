class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k  = k
        self.que = deque()
        
    def consec(self, num: int) -> bool:
        if num == self.value:
            self.que.append(num)
        if len(self.que) == self.k:
            self.que.popleft()
            return True
        if num != self.value:
            self.que = deque()
            return False
        return False    
      

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)