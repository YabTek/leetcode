class MyCircularDeque:

    def init(self, k: int):
        self.k = k
        self.arr = []
     
    def insertFront(self, value: int) -> bool:
    
        if self.isFull():
            return False
        else:
            self.arr.insert(0,value)      
            return True        
       
    def insertLast(self, value: int) -> bool:
     
        if len(self.arr) >= self.k:
            return False
        else:
            self.arr.append(value)
            return True
        
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            del  self.arr[0]
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            del self.arr[-1]
            return True
    def getFront(self)-> int:
        if not self.isEmpty(): 
            return self.arr[0]
        else:
            return -1     

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.arr[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if len(self.arr) == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        return len(self.arr) == self.k
         
   


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()