# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        self.inorder(root, res)
        return self.build(0, len(res)-1, res)
    def inorder(self, node, res):
        if not node:
            return
        self.inorder(node.left, res)
        res.append(node.val)
        self.inorder(node.right, res)

    def build(self, left, right, res):
        if left  > right:
            return
        mid = (left + right)//2
        root = TreeNode(res[mid])
        root.left = self.build(left, mid-1, res)
        root.right = self.build(mid + 1, right, res)
        return root



