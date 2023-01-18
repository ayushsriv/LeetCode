# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return None
        curr = Tree = TreeNode()
        curr.val = preorder.pop(0)
        index = inorder.index(curr.val)
        curr.left = self.buildTree(preorder, inorder[:index])
        curr.right = self.buildTree(preorder, inorder[index+1:])
        return Tree