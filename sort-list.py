#Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        temp = head
        while temp:
            lst.append(temp.val)
            temp=temp.next
        lst.sort()
        cur = tempNode= ListNode(0)

        for item in lst:
            cur.next = ListNode(item)
            cur = cur.next

        return tempNode.next
    # while temp and temp.next:
         #   Next = temp.next
        #    if Next.val < temp.val:
          #      Next.val,temp.val = temp.val,Next.val
          #      Next = Next.next
         #   temp = temp.next
       # return head