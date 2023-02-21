# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = head
        end = None
        prev = None
        
        i = 0
        j = 0
        
        if head == None or head.next == None:
            return head
        
        for _ in range(left-1):
            prev = start
            start = start.next
            i += 1
   
        for _ in range(right-1):
            j += 1
            
        cur = start
        for _ in range(i,j+1):
            succeeding = start.next
            start.next = end
            end = start
            start = succeeding
            
        if cur:
            cur.next = start
            if prev is None:       
                head = end
            else:
                prev.next = end
 
        return head
            
  