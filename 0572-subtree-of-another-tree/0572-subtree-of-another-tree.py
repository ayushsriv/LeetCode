# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root, subRoot):
        if root and subRoot:
            return root.val==subRoot.val and self.helper(root.left, subRoot.left) and self.helper(root.right, subRoot.right)
        return root is subRoot
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if root.val == subRoot.val:
            if self.helper(root, subRoot):
                return True
        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)
        return l or r
