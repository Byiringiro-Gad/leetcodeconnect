# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dict1 = {}
        curr = head
        while curr:
            dict1[curr.val] = dict1.get(curr.val, 0) + 1
            curr = curr.next
        dummy = ListNode(0)
        tail = dummy
        cur = head
        while cur:
            if dict1[cur.val] == 1:
                tail.next = cur
                tail = tail.next
            cur = cur.next
        tail.next = None
        return dummy.next

            