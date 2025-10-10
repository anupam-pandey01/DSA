# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        while (curr is not None):
            length += 1
            curr = curr.next
        
        m = length // 2
        middle_node = head

        for i in range(0, m):
            middle_node = middle_node.next
        
        return middle_node

        
