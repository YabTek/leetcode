# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        holder = 0
        head = ListNode()
        tail = head

        while l1 != None or l2 != None or holder:
            if l1 is not None:
                operandA = l1.val
            else:
                operandA = 0
            if l2 is not None:
                operandB = l2.val
            else:
                operandB = 0

            operandC = operandA + operandB + holder
            holder = operandC//10
            operandC %= 10

            tail.next = ListNode(operandC)
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next