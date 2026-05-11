# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        max_length = self.depthTree(root.left) + self.depthTree(root.right)
        max_length = max(self.diameterOfBinaryTree(root.left), max_length)
        max_length = max(self.diameterOfBinaryTree(root.right), max_length)
        
        return max_length
    
    def depthTree(self, root) -> int:
        if root is None:
            return 0

        left = self.depthTree(root.left)
        right = self.depthTree(root.right)
        return max(left, right) + 1