# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        
        while cur and cur.next:
            new_node = ListNode(gcd(cur.val, cur.next.val))
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next
            
        return head
            
        
