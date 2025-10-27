# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lo, hi = (p.val, q.val) if p.val < q.val else (q.val, p.val)
        node = root
        while node:
            if node.val > hi:
                node = node.left
            elif node.val < lo:
                node = node.right
            else:
                return node
        return None  # defensive; LC constraints mean we never hit this
