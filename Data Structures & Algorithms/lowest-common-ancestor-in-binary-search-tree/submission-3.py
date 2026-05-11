# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None

        if root == q and root == p:
            return root

        parent = root
        left   = root.left if not None else None
        right  = root.right if not None else None
        result = [parent.val, left.val if left else None, right.val if right else None]

        if q in result and p in result:
            min_res = min(result)
            return p if p.val == min_res else q if q.val == min_res else parent.val
        else:
            min_left = self.lowestCommonAncestor(left, p, q)
            min_right = self.lowestCommonAncestor(right, p, q)
            return min_left if min_left else min_right
            