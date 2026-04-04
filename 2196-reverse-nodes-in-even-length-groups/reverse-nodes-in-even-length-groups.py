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
        
        prev_group_end = dummy
        curr = head
        group_size = 1
        
        while curr:
            count = 0
            temp = curr
            while temp and count < group_size:
                temp = temp.next
                count += 1
            
            if count % 2 == 0:
                new_head, next_group_start = reverse(curr, count)
                
                prev_group_end.next = new_head
                curr.next = next_group_start
                
                prev_group_end = curr
                curr = next_group_start
            else:
                for _ in range(count):
                    prev_group_end = curr
                    curr = curr.next
            
            group_size += 1
        
        return dummy.next