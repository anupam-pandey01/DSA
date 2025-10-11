# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # temp = head 
        # stack = []
        # while(temp != None):
        #     stack.insert(0, temp.val)
        #     temp = temp.next
        
        # curr = head
        # i = 0
        # while(curr != None):
        #     curr.val = stack[i]
        #     curr = curr.next
        #     i+=1
        
        # return head

        curr = head
        stack = []

        while(curr is not None):
            stack.append(curr.val)
            curr = curr.next
        
        curr = head
        while(curr is not None):
            e = stack.pop()
            curr.val = e
            curr = curr.next
        
        return head
            
        
        