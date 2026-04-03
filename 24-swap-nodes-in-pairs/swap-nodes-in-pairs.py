# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        swaped = False
        while curr and curr.next:
            if not swaped:
                value = curr.val
                curr.val = curr.next.val
                curr.next.val = value
                swaped = True
            curr = curr.next
            curr = curr.next
            swaped = False
        return head
        

