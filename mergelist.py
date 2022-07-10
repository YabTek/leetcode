#Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1 , list2):
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            if list1.val < list2.val:
                sorted = list1
                sorted.next = self.mergeTwoLists(list1.next,list2)
            else:
          
                sorted = list2               
                sorted.next = self.mergeTwoLists(list1,list2.next)
        return sorted