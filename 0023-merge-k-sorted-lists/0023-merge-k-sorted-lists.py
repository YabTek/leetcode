# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        firstlist = ListNode()
        for lst in lists:
            firstlist.next = Solution.mergetwo(self,firstlist.next, lst)
        return firstlist.next
            
    def mergetwo(self,list1,list2):
        tempNode = ListNode(0)
        voidNode = tempNode
        while list1 and list2:
            if list1.val < list2.val:
                voidNode.next = list1
                list1 = list1.next
            else:
                voidNode.next = list2
                list2 = list2.next
            voidNode = voidNode.next
        if list1 is None:
            voidNode.next = list2
        else:
            voidNode.next = list1
       
        return tempNode.next