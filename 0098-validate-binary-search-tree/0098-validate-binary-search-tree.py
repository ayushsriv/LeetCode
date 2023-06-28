# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(low, high, root):
            if not root: return True

            if root.val <= low or root.val >= high:
                return False 

            return helper(root.val, high, root.right) and helper(low, root.val, root.left)

        return helper(float('-inf'), float('inf'), root)

    




        