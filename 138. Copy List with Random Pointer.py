"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        mapp = {}

        temp = head
        while temp:
            mapp[temp] = Node(temp.val)
            temp = temp.next

        
        temp = head
        while temp:
            mapp[temp].next = mapp.get(temp.next)
            mapp[temp].random = mapp.get(temp.random)
            temp = temp.next

        return mapp[head]



       
        