# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tot = 0
        ans = ListNode()
        temp_ans = ans
        
        while head:
            if head.val == 0 and tot != 0:
                temp_ans.next = ListNode(tot)
                temp_ans = temp_ans.next
                tot = 0
            tot += head.val
            head = head.next
            
        return ans.next
        