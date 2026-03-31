# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        self.helper(root, res)
        return self.merge(0, len(res)-1, res)
    def helper(self, root, res):
        if not root:
            return
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)
    def merge(self, left, right, res):
        if left > right:
            return
        mid = (left + right)// 2
        root = TreeNode(res[mid])
        root.left = self.merge(left, mid-1, res)
        root.right = self.merge(mid+1, right, res)
        return root
