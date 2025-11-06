# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
    #    s = set()
    #    curr = head

    #    while(curr != None):
    #     if(curr in s):
    #         return True
    #     else: 
    #         s.add(curr)
    #         curr = curr.next
       
    #    return False

        slow = head
        fast = head

        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

            if(slow == fast):
                return True
        
        return False

       
