# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        current = root

        while current:
            if min(p.val, q.val) > current.val:
                current = current.right
            elif max(p.val, q.val) < current.val:
                current = current.left
            else:
                return current
        
        