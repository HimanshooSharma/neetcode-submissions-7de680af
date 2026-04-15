# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        good_nodes = 0

        def dfs(node, max_so_far=float('-inf')):

            if not node:
                return

            nonlocal good_nodes

            if node.val >= max_so_far:
                good_nodes += 1

            max_so_far = max(node.val, max_so_far)
                
            dfs(node.left, max_so_far)
            dfs(node.right, max_so_far)
        
        dfs(root)
        return good_nodes


