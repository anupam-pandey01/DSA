# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        arr.sort()
        curr = head

        while curr:
            e = arr.pop(0)
            curr.val = e
            curr = curr.next
        
        return head