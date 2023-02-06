# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Go down to left node and then bubble up from there
        def inOrder(root,res):
            if root.left:
                inOrder(root.left,res)
            res.append(root.val)
            if root.right:
                inOrder(root.right,res)
        ret = []
        inOrder(root,ret)
        return ret[k-1]