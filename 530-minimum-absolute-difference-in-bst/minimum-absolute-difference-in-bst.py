# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []
        def helper(node):
            if not  node:
                return None

            helper(node.left)
            res.append(node.val)
            helper(node.right)
        helper(root)
        r = 1
        diff = float("inf")
        for i in range(len(res)-1):
            curr_min = res[i] - res[r]
            diff = min(diff, abs(curr_min))
            r += 1
        return diff





        
