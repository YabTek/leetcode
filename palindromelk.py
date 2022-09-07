# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        store = []
        while temp:
            store.append(temp.val)  
            temp = temp.next
        store2 = store.copy()
        store2.reverse()
        if store==store2:
            return True
        return False