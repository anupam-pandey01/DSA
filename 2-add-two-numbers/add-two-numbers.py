# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = carry = 0
        dummy = ListNode()
        curr = dummy

        while(l1 or l2 or carry):
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            node_val = total % 10
            carry = total // 10

            new_node = ListNode(node_val)
            curr.next = new_node

            curr = curr.next
        
        return dummy.next