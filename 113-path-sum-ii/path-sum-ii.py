# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def helper(node, remaining, path):
            if not node:
                return
            path.append(node.val)
            remaining -= node.val

            if not node.left and not node.right and remaining == 0:
                res.append(path[:])
            else:
                helper(node.left, remaining, path)
                helper(node.right, remaining, path)
            path.pop()
        
        helper(root, targetSum, [])
        return res
