# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr[k-1], arr[-k] = arr[-k], arr[k-1]
        dummy = ListNode(0)
        head = dummy
        i = 0
        while i < len(arr):
            head.next = ListNode(arr[i])
            head = head.next
            i += 1
        return dummy.next
