# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
          
        store = []
        for lst in lists:
            while lst is not None:
                store.append(lst.val)
                lst=lst.next
        store.sort()
   
        tempNode = ListNode(0)
        temp = tempNode
        for num in store:
            temp.next = ListNode(num)
            temp = temp.next
        return tempNode.next