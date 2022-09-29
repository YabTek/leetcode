#Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

            
        tempNode = ListNode(0,head)
        pre = tempNode
        now = head
        while now is not None and now.next is not None:
            first = now.next.next
            second = now.next
            second.next = now
            now.next=first
            pre.next = second
            pre=now
            now =first
        return tempNode.next