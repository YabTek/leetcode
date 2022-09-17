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
          
        heap = []

        for lst in lists:
            print(lst)
            while lst is not None:
                heapq.heappush(heap,lst.val)
                lst=lst.next
               
        result = heapq.nsmallest(len(heap),heap)
   
        voidNode = ListNode(0)
        temp = voidNode
        for num in result:
            temp.next = ListNode(num)
            temp = temp.next
        return voidNode.next