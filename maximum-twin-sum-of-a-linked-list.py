# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst = []
        while head:
            lst.append(head.val)
            
            head=head.next
        ans = [0 for _ in range(len(lst)//2)]
        start = 0
        end = len(lst)-1
        while start < end:
            ans[start] = lst[start] + lst[end]
            start+=1
            end-=1                       
        return max(ans)