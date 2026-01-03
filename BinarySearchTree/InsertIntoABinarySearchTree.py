# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root == None:
            return TreeNode(val)

        curr_node = root

        while curr_node:

            if curr_node.left == None and val < curr_node.val:
                curr_node.left = TreeNode(val)
                break

            if curr_node.right == None and val > curr_node.val:
                curr_node.right = TreeNode(val)
                break

            if val < curr_node.val:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

            if curr_node == None:
                curr_node = TreeNode(val)
                break

        return root