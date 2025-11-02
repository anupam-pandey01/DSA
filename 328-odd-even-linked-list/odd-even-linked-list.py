# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None or head.next is None):
            return head
        
        odd = head
        even = head.next
        even_head = even

        while(even != None and even.next != None):
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = even_head
        return head
        
        # order = []
        # temp = head

        # while(temp != None):
        #     order.append(temp.val)
        #     temp = temp.next.next if temp.next else None
        

        # temp = head.next

        # while(temp != None):
        #     order.append(temp.val)
        #     temp = temp.next.next if temp.next else None
        
        # temp = head
        # i = 0
        # while(temp != None):
        #     temp.val = order[i]
        #     i+=1
        #     temp = temp.next
        
        # return head
