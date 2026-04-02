# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        set1 = set(nums)
        dummy = ListNode(0)
        tail = dummy
        curr = head
        while curr:
            if curr.val not in set1:
                tail.next = curr
                tail = tail.next
            curr = curr.next
        tail.next = None
        return dummy.next