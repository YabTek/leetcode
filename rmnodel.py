#Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=0
        value=head
        while value is not None:
            value=value.next
            i+=1
        val=i-n+1
        linked=prev=ListNode(None)
       # prev=ListNode(None)

        linked.next=head
        value=head

        i=0
        while value:
            if i==val-1:
                prev.next=value.next
                break
            i+=1
            prev=value
            value=value.next
        return linked.next