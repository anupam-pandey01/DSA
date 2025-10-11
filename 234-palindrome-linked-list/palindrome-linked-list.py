# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        stack = []
        while(curr != None):
            stack.append(curr.val)
            curr = curr.next
        
        curr = head
        for i in range(len(stack)):
            e = stack.pop()
            if e != curr.val:
                return False
            curr = curr.next
        
        return True
