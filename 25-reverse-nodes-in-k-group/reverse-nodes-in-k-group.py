# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getkth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            kth = getkth(prev_group, k)
            if not kth:
                break

            next_group = kth.next
            prev = next_group
            curr = prev_group.next
            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp
        
        return dummy.next
