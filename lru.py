class LRUCache:

    def init(self, capacity: int):
        self.length = 0
        self.capacity = capacity
        self.LRU= collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.LRU:
            self.LRU.move_to_end(key, last=False)
            return self.LRU[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.LRU:
            if self.length == self.capacity:
                self.LRU.popitem()
            else:
                self.length += 1
        self.LRU[key] = value
        self.LRU.move_to_end(key, last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)