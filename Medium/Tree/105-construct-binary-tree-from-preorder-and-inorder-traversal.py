# Problem: 105 – construct binary tree from preorder and inorder traversal
# Difficulty: Medium
# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def buildTree(preorder,pl,pr,inorder,il,ir):
            if pl>=pr or il>=ir:
                return None
            root = TreeNode(preorder[pl])
            # print(help(list))
            root_inorder = inorder.index(root.val,il,ir)

            num_in_left = root_inorder-il
            num_in_right = ir - root_inorder

            root.left = buildTree(preorder,pl+1,pl+1+num_in_left,inorder,il,root_inorder)
            root.right = buildTree(preorder,pl+1+num_in_left,pr,inorder,root_inorder+1,ir)
            return root
        
        return buildTree(preorder,0,len(preorder),inorder,0,len(inorder))


        # if not inorder or not preorder:
        #     return None
        # root = TreeNode(preorder[0])
        # # print(help(list))
        # root_inorder = inorder.index(root.val)

        # root.left = self.buildTree(preorder[1:root_inorder+1],inorder[:root_inorder])
        # root.right = self.buildTree(preorder[root_inorder+1:],inorder[root_inorder+1:])
        # return root