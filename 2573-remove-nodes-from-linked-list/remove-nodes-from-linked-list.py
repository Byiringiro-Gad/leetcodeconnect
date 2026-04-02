# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            while stack and stack[-1] < curr.val:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next
        self.dummy = ListNode(0)
        self.head = self.dummy
        def helper(index, stack):
            if index > len(stack)-1:
                return None
            node = ListNode(stack[index])
            self.head.next = node
            self.head = self.head.next
            helper(index + 1, stack)
        helper(0, stack)
        return self.dummy.next