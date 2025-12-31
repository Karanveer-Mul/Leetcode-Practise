# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        stack = [(root, False)]
        max_height_dict = {}
        diameter = 0

        while stack:

            node, visited = stack.pop()

            if not visited:
                stack.append((node, True))

                if node.left:
                    stack.append((node.left, False))

                if node.right:
                    stack.append((node.right, False))

            else:
                left_height = 0
                if node.left != None:
                    left_height = max_height_dict.pop(node.left)

                right_height = 0
                if node.right != None:
                    right_height = max_height_dict.pop(node.right)

                diameter = max(diameter, left_height + right_height)
                max_height_dict[node] = max(left_height, right_height) + 1
        
        return diameter