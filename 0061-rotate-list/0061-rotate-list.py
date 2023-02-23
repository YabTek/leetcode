# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        right = head
        left = head
        temp = head
        size = 0
        
        if not head or not head.next or k == 0:
            return head
        
        while temp:
            size += 1
            temp = temp.next
        
        k %= size
        
        while k > 0:
            right = right.next
            k -= 1
      
        while right and right.next:
            left = left.next
            right = right.next
        right.next = head
        head = left.next
        left.next = None
           
        return head
        