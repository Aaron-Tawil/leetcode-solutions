# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#leetcode 572 - subtree-of-another-tree
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isIdentical(s,t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return s.val == t.val and isIdentical(s.left,t.left) and isIdentical(s.right,t.right)
        
        def isSubtreeDfs( root, subRoot):
            if not root:
                return False
            return isIdentical(root,subRoot) or isSubtreeDfs(root.left,subRoot) or isSubtreeDfs(root.right,subRoot)
        
        return isSubtreeDfs( root, subRoot)
        