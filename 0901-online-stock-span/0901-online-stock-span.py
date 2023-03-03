class StockSpanner:

    def __init__(self):
        self.stk = []
        self.dictionary = {}
        
    def next(self, price: int) -> int:
        span = 1
        
        while self.stk and price >= self.stk[-1]:
            span += self.dictionary[self.stk.pop()]
        self.stk.append(price)
        self.dictionary[price] = span
        
        return span
        
   
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)