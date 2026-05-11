# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False 
        print(self.height(root.left))
        print(self.height(root.right))
        return True if self.height(root.left) - self.height(root.right) <= 1 else False

    def height(self, root):
        return 0 if root is None else max(self.height(root.left), self.height(root.right)) + 1