# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        succeeding = None
        preceding = None
        
        while(head):
            succeeding = head.next
            head.next = preceding
            
            preceding =  head
            head = succeeding
            
        return preceding