# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left: left = root.left
        if root.right: right = root.right

        if root.left and root.right:
            root.left = self.invertTree(right)
            root.right = self.invertTree(left)
        elif not root.left and root.right:
            root.left = self.invertTree(right)
            root.right = None
        elif not root.right and root.left:
            root.right = self.invertTree(left)
            root.left = None
        else:
            return None
        
        return root
        