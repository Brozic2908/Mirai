# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False

        if root.val != subRoot.val:
            return self.isSubtree(root.left, subRoot) and self.isSubtree(root.right, subRoot)
        
        if root.val == subRoot.val:
            same = self.isSameTree(root, subRoot)
            return same
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p: return True
        elif (not q and p) or (not p and q): return False
        return q.val == p.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)