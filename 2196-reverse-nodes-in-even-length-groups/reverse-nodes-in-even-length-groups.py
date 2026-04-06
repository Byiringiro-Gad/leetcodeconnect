# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head, k):
            prev = None
            curr = head
            while k > 0:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                k -= 1
            return prev, curr
        dummy = ListNode(0)
        dummy.next = head
        prev_end = dummy

        curr = head
        size = 1
        while curr:
            temp = curr
            cnt = 0
            while temp and cnt < size:
                temp = temp.next
                cnt += 1

            if cnt % 2 == 0:
                new_head, next_start = reverse(curr, cnt)

                prev_end.next = new_head
                curr.next = next_start
                prev_end = curr
                curr = next_start
            else:
                for _ in range(cnt):
                    prev_end = curr
                    curr = curr.next
            size += 1
        return dummy.next