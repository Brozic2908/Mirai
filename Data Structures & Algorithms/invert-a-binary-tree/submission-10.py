# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        left = root.left
        right = root.right

        if root.left and root.right:
            root.left = self.invertTree(right)
            root.right = self.invertTree(left)
        elif root.right:
            root.left = self.invertTree(right)
            root.right = None
        else:
            root.right = self.invertTree(left)
            root.left = None
        
        return root
        