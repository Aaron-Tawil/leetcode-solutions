# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        #base case 
        if not root or root==p or root==q:
            return root

        # search p or q in the left and right
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        # q is in one side and p in the other then root is the lca
        if right and left:
            return root
        
        # bubble up the result
        return left if left else right
        