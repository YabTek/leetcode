class RecentCounter:

    def __init__(self):
        self.lst = []
        self.left = 0 
       
    def ping(self, t: int) -> int:
        ranges = [t-3000,t]
        self.lst.append(t)
        
        if ranges[0] <= self.lst[self.left]:
            return len(self.lst) - self.left
        else:
            while  ranges[0] > self.lst[self.left]:
                self.left += 1
            return len(self.lst) - self.left
            
        
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)