# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root, subRoot):
        if not root and not subRoot:
            return True 
        if not root or not subRoot:
            return False 
        if root.val != subRoot.val:
             return False
        left = right = True
        left = self.helper(root.left, subRoot.left)
        right = self.helper(root.right, subRoot.right)
        return left and right
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return 
        if root.val == subRoot.val:
            if self.helper(root, subRoot):
                return True
        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)
        return l or r
