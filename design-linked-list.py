class MyLinkedList:
    class Node:

         def init(self,data,nxt):

            self.data = data

            self.nxt = None
    def init(self):
        self.head = None
        self.end = None
        self.amount = 0

    def get(self, index: int) -> int:
        
        value = self.head
        i = 0
        while i<index:
            value= value.nxt
            i+=1
        return value.data
        if index >= self.amount:
            return -1
        

    def addAtHead(self, val: int) -> None:
        add_node = self.Node(val,None)
        add_node.nxt = self.head
        self.head = add_node
        
        self.amount+=1
    def addAtTail(self, val: int) -> None:
        add_node = self.Node(val,None)
        if self.head is None:
            self.head = add_node
            return
        temp = self.head
        while temp.nxt is not None:
            temp = temp.nxt
        temp.nxt = add_node
        self.amount+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        add_node = self.Node(val,None) 
        if index > self.amount:
            return


        elif index == self.amount:

            return self.addAtTail(val)
        elif index == 0:

                self.addAtHead(val)


        elif index < self.amount and index > 0:

            
                


                add_node = self.Node(val, None)

                now = self.head

                for i in range(index - 1):

                    now = now.nxt

                add_node.nxt = now.nxt

                now.nxt = add_node

                

                self.amount += 1

           

        

       
    
    def deleteAtIndex(self, index: int) -> None:
        if index <= self.amount- 1 and index >= 0:

            

            if index == 0:

                self.head = self.head.nxt

            else:

                prev = None

                curr = self.head

                for i in range(index):

                    prev = curr

                    curr = curr.nxt

                

                prev.nxt = curr.nxt



                if index == self.amount - 1:

                    self.end = prev

                

            self.amount-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
#obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)