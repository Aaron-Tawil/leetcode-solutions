# Problem: 104 – maximum depth of binary tree
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root: return 0
    #     q = deque([root])
    #     d = 0
    #     while q:
    #         d+=1
    #         for _ in range(len(q)):
    #             node = q.popleft()
    #             if node.left: q.append(node.left)
    #             if node.right: q.append(node.right)
    #     return d
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        s = [(root,1)]
        md = 0
        while s :
            node,d = s.pop()
            md = max(md,d)
            if node.left: s.append((node.left,d+1))
            if node.right: s.append((node.right,d+1))      
        return md

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     def go(node):
    #         if not node: return 0
    #         return max(go(node.left),go(node.right)) +1   
        
    #     return go(root)