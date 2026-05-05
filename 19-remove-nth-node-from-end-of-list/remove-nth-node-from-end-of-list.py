# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n + 1):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next
        # count = 0
        # curr = head

        # while curr:
        #     count += 1
        #     curr = curr.next
        
        # curr = head
        # prev = None
        # remove_len = count - n
        
        # for _ in range(remove_len):
        #     prev = curr
        #     curr = curr.next
        
        # if remove_len == 0:
        #     head = head.next
        # else:
        #     prev.next = curr.next

        
        # return head