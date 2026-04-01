# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dum1 = ListNode(0)
        dum2 = ListNode(0)
        dum3 = ListNode(0)

        tail1 = dum1
        tail2 = dum2
        tail3 = dum3

        curr = head
        cnt = 1

        while curr:
            if cnt < left:
                tail1.next = curr
                tail1 = tail1.next
            elif cnt >= left and cnt <= right:
                tail2.next = curr
                tail2 = tail2.next
            else:
                tail3.next = curr
                tail3 = tail3.next
            curr = curr.next
            cnt += 1

        tail1.next = None
        tail2.next = None
        tail3.next = None
        prev = None
        curr = dum2.next

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt    
      
        tail1.next = prev
        dum2.next.next = dum3.next
        return dum1.next

        