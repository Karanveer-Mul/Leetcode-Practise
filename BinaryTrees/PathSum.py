# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root == None:
            return False

        def helper(node, curSum):
            curSum += node.val

            if node.left == None and node.right == None and curSum == targetSum:
                return True

            left_possible = False
            right_possible = False
            if node.left:
                left_possible = left_possible or helper(node.left, curSum)
            if node.right:
                right_possible = right_possible or helper(node.right, curSum)

            return left_possible or right_possible

        return helper(root, 0)