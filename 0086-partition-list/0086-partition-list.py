# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp = head
        less_than = ListNode()
        greater_than = ListNode()
        dummy_less = less_than
        dummy_greater = greater_than
        
        while temp:
            if temp.val >= x:
                greater_than.next = temp
                greater_than = greater_than.next 
            else:
                less_than.next = temp
                less_than = less_than.next
            temp = temp.next
        less_than.next = dummy_greater.next
        greater_than.next = None
        
        return dummy_less.next

       
       