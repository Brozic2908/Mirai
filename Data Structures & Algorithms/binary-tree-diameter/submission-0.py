# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_length = diameterOfBinaryTree(root.left) + diameterOfBinaryTree(root.right)
        return depthTree(root)
    
    def depthTree(self, root) -> int:
        left = self.depthTree(root.left)
        right = self.depthTree(root.right)
        return max(left, right) + 1