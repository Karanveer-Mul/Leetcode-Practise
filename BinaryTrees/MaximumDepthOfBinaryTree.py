# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        def helper(node):
            if node == None:
                return float('-inf')

            if node.left == None and node.right == None:
                return 1

            left_depth = helper(node.left)
            right_depth = helper(node.right)

            return max(left_depth, right_depth) + 1

        return helper(root)