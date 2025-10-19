# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0  # stores the maximum diameter found so far (in edges)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def height(node: 'TreeNode') -> int:
            if not node:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            # Update diameter candidate passing through this node
            self.ans = max(self.ans, lh + rh)
            # Return height of current node (in edges)
            return 1 + max(lh, rh)

        height(root)
        return self.ans
        